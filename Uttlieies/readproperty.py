import configparser


config = configparser.RawConfigParser()
config.read("Cong/Config.ini")


class ReadConfig:

    @staticmethod
    def get_url():
        url = config.get("common info", "baseurl")
        return url

    @staticmethod
    def get_username():
        username = config.get("common info", "username")
        return username

    @staticmethod
    def get_password():
        password = config.get("common info", "password")
        return password

    @staticmethod
    def get_password2():
        password2 = config.get("common info", "password2")
        return password2

