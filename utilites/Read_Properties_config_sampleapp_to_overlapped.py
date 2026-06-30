import configparser

class Read_properties_sampleapp_to_overlapp:
    config=configparser.ConfigParser()
    config.read(".\\Configurations\\config_sampleapp_to_overlapped.ini")

    @staticmethod
    def get_url_sampleapp():
        return Read_properties_sampleapp_to_overlapp.config.get("URL","sampleapp")


    @staticmethod
    def get_url_mouseover():
        return Read_properties_sampleapp_to_overlapp.config.get("URL", "mouseover")

    @staticmethod
    def get_url_nbsp():
        return Read_properties_sampleapp_to_overlapp.config.get("URL", "nbsp")

    @staticmethod
    def get_url_overlapped():
        return Read_properties_sampleapp_to_overlapp.config.get("URL", "overlapped")

