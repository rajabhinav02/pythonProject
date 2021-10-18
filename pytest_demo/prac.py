import inspect
import logging


def customlog(loglevel):
    tcname = inspect.stack()[1][3]
    logger = logging.getLogger(tcname)
    logger.setLevel(logging.DEBUG)
    filehandler = logging.FileHandler("{0}.log".format(tcname), mode="a")
    filehandler.setLevel(loglevel)
    format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    filehandler.setFormatter(format)
    logger.addHandler(filehandler)
    return logger


