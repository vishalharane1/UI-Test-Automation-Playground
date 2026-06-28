import configparser

class Read_Config_for_dynamic_visible:
    config=configparser.ConfigParser()
    config.read(".\\Configurations\\config_dynamictable_to_visibility.ini")

    @staticmethod
    def get_url_dynamic_table():
        return Read_Config_for_dynamic_visible.config.get("URL","dynamictable")



