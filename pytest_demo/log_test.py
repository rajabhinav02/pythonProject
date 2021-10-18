import logging

logger=logging.getLogger(__name__)

fileloc=logging.FileHandler("loggi.log")
format=logging.Formatter("%(asctime)s : %(levelname)s : %(message)s : %(name)s")
fileloc.setFormatter(format)

logger.addHandler(fileloc)
logger.setLevel(logging.DEBUG)

logger.debug("This is just f")