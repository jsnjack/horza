import os


class Settings(object):
    db_path = os.path.join(os.path.expanduser("~"), ".horza")
    db_url = "sqlite:///%s/horza.sqlite3" % db_path
    db_echo = True
