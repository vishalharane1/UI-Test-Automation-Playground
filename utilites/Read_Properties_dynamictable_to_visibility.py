import configparser

class Read_Config_for_dynamic_visible:
    config=configparser.ConfigParser()
    config.read(".\\Configurations\\config_dynamictable_to_visibility.ini")

    @staticmethod
    def get_url_dynamic_table():
        return Read_Config_for_dynamic_visible.config.get("URL","dynamictable")

    @staticmethod
    def get_url_verifytext():
        return Read_Config_for_dynamic_visible.config.get("URL","verifytext")

    @staticmethod
    def get_url_progressbar():
        return Read_Config_for_dynamic_visible.config.get("URL", "progressbar")

    @staticmethod
    def get_url_visibility():
        return Read_Config_for_dynamic_visible.config.get("URL","visibility")







