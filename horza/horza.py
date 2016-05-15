#!/usr/bin/env python3
import sys

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '3.0')
from gi.repository import Gtk


class HorzaWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        self.app = app

        Gtk.Window.__init__(self, title="horza", application=app)
        self.set_wmclass("horza", "horza")


class HorzaApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        self.main_window = HorzaWindow(self)
        self.main_window.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)


if __name__ == '__main__':
    app = HorzaApplication()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)
