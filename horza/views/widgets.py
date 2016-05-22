import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '3.0')
from gi.repository import Gtk


class RepositoryWidget(Gtk.Box):
    """
    Widget that represents repository on the main window
    """
    def __init__(self, repo_id, repo_path):
        super().__init__()

        self.repo_id = repo_id
        self.repo_path = repo_path

        self.set_orientation(Gtk.Orientation.VERTICAL)

        repo_name = Gtk.Label()
        repo_name.set_text(self.repo_path)
        repo_name.set_name("repository_label")
        self.pack_start(repo_name, True, True, 2)
