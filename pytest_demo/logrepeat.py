import inspect
import logging

tcname=inspect.stack()[1][3]
logger=logging.getLogger(__name__)


fileloc= logging.FileHandler("loggyyyy.log")

format=logging.Formatter("%(asctime)s : %(levelname)s :  %(name)s : %(message)s")

fileloc.setFormatter(format)

logger.addHandler(fileloc)

logger.setLevel(logging.DEBUG)