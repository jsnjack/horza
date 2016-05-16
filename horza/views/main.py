import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '3.0')
from gi.repository import Gtk


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
        print("1")
