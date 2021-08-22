import configparser


class _Config:
    def __init__(self):
        self.configuration = configparser.ConfigParser()
        self.configuration.read("./config.ini")


config = _Config().configuration
