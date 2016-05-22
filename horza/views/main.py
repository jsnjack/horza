import logging
import os

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '3.0')
from gi.repository import Gtk

from sqlalchemy.exc import IntegrityError

from horza import session
from horza.models import Repository


logger = logging.getLogger(__name__)


class HorzaWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        self.app = app

        Gtk.Window.__init__(self, title="horza", application=app)
        self.set_wmclass("horza", "horza")

        header_bar = Gtk.HeaderBar()
        header_bar.set_show_close_button(True)

        add_repo_button = Gtk.Button.new_with_label("Add")
        add_repo_button.set_tooltip_text("Add repository")
        add_repo_button.connect("clicked", self.on_add_repo_button_clicked)
        header_bar.pack_start(add_repo_button)

        self.set_titlebar(header_bar)

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
