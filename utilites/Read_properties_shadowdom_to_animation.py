import configparser

class Read_url_showdown_to_animation:
    config=configparser.ConfigParser()
    config.read(r"Configurations/config_shadowdom_to_animation.ini")

    @staticmethod
    def get_showdown_url():
        return Read_url_showdown_to_animation.config.get("URL","shadowdom")

