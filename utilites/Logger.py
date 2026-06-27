import logging

class Log_genrator_class:
    @staticmethod
    def logs_method(path_File):
        log_file = logging.FileHandler(path_File)
        # log_file=logging.FileHandler(r"Logs/UITesting_Playgrond.log")
        log_formate=logging.Formatter("%(asctime)s:%(levelname)s:%(funcName)s:%(lineno)d:%(message)s")
        log_file.setFormatter(log_formate)
        logger=logging.getLogger()
        logger.addHandler(log_file)
        logger.setLevel(logging.INFO)
        return logger

