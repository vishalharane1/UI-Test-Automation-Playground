import configparser

class Readconfig:
    config=configparser.ConfigParser()
    config.read(".\\Configurations\\config.ini")

    @staticmethod
    def get_dynamic_url():
        return Readconfig.config.get('urls','dynamicid_url')

    @staticmethod
    def get_classattr():
        return Readconfig.config.get("urls","classattr")

    @staticmethod
    def get_hiddenlayers():
        return Readconfig.config.get("urls","hiddenlayers")

    @staticmethod
    def get_ajex_url():
        return Readconfig.config.get("urls","ajax")

    @staticmethod
    def get_client_delay_url():
        return Readconfig.config.get("urls","clientdelay")
    @staticmethod
    def get_click_url():
        return Readconfig.config.get("urls","click")

