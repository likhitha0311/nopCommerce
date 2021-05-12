import configparser

config=configparser.RawConfigParser()
config.read("./Configurations/config.INI")
config.sections()

class ReadConfig:

    @staticmethod
    def getApplicationUrl():
        url=config.get('Common info', 'url')
        return url

    @staticmethod
    def getUsername():
        username = config.get('Common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('Common info', 'password')
        return password