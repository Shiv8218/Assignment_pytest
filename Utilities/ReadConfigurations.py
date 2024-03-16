from configparser import ConfigParser


def readconfig(category,key):
    config = ConfigParser()
    config.read("Configuration/config.ini")
    return config.get(category,key)