import logging
import os

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '3.0')
from gi.repository import Gtk, Gdk

from sqlalchemy.exc import IntegrityError

from horza import session, settings
from horza.models import Repository
from horza.views.widgets import RepositoryWidget


logger = logging.getLogger(__name__)


class HorzaWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        self.app = app

        Gtk.Window.__init__(self, title="horza", application=app)

        self.build_interface()
        self.load_repositories()

    def build_interface(self):
        """
        Populate window with widgets
        """
        self.set_wmclass("horza", "horza")
        self.set_border_width(2)
        self.set_default_size(settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)

        scrolled_window = Gtk.ScrolledWindow()
        main_box = Gtk.Box()
        main_box.set_orientation(Gtk.Orientation.HORIZONTAL)
        main_box.set_homogeneous(True)
        scrolled_window.add(main_box)

        self.repository_box = Gtk.Box()
        self.repository_box.set_orientation(Gtk.Orientation.VERTICAL)
        main_box.pack_start(self.repository_box, True, True, 2)

        header_bar = Gtk.HeaderBar()
        header_bar.set_show_close_button(True)

        add_repo_button = Gtk.Button.new_with_label("Add")
        add_repo_button.set_tooltip_text("Add repository")
        add_repo_button.connect("clicked", self.on_add_repo_button_clicked)
        header_bar.pack_start(add_repo_button)

        self.set_titlebar(header_bar)
        self.add(scrolled_window)

        css_provider = Gtk.CssProvider()
        css_provider.load_from_path(
            os.path.join(settings.BASE_DIR, "views/styles.css")
        )
        screen = Gdk.Screen.get_default()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(
            screen,
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    def load_repositories(self):
        """
        Load repositories from the database and put them on the window
        """
        query = session.query(Repository)
        for item in query.all():
            self.repository_box.pack_end(
                RepositoryWidget(item.id, item.path),
                True, True, 2
            )

    def on_add_repo_button_clicked(self, target):
        """
        Add new repository
        """
        dialog = Gtk.FileChooserDialog(
            "Add repository", self, Gtk.FileChooserAction.SELECT_FOLDER,
            ("_Cancel", Gtk.ResponseType.CANCEL,
             "_Open", Gtk.ResponseType.OK)
        )

        open_button = dialog.get_header_bar().get_children()[1]
        open_button.get_style_context().add_class("suggested-action")

        dialog.set_current_folder(os.path.expanduser("~"))

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            path = dialog.get_filename()
            repo = Repository(path=path)
            session.add(repo)
            try:
                session.commit()
            except IntegrityError:
                logger.debug("Path %s is already in the database" % path)
            else:
                logger.debug("Path %s created with id %s" % (path, repo.id))
        dialog.destroy()
