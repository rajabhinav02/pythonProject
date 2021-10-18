import inspect
import logging
class logdemotest:
    def log(self):
        tcname= inspect.stack()[1][3]
        logger=logging.getLogger(tcname)

        filelog=logging.FileHandler("logeee.log")

        Format=logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

        filelog.setFormatter(Format)

        logger.addHandler(filelog)

        logger.setLevel(logging.DEBUG)

        return logger