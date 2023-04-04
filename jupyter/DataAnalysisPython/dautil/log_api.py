from pkg_resources import get_distribution
from pkg_resources import resource_filename
import logging
import logging.config
import pprint
from appdirs import AppDirs
import os

def get_logger(name):
    log_config = resource_filename(__name__, 'long.conf')
    logging.config.fileConfig(log_config)
    logger = logging.getLogger(name)
    return logger

def shorten(module_name):
    dot_i = module_name.find('.')
    return module_name[:dot_i]

def log(modules, name):
    skiplist = ['pkg_resources', 'distutils']
    logger = get_logger(name)
    logger.debug('Inside the log function')
    for k in modules.keys():
        str_k = str(k)
        if '.version' in str_k:
            short = shorten(str_k)
        if short in skiplist:
            continue
        try:
            logger.info('%s=%s' % (short,
            get_distribution(short).version))
        except ImportError:
            logger.warn('Could not impport', short)

class VersionsLogFileHandler(logging.FileHandler):
    def __init__(self, fName):
        dirs = AppDirs("PythonDataAnalysisCookbook",
        "Ivan Idris")
        path = dirs.user_log_dir
        print(path)
        if not os.path.exists(path):
            os.mkdir(path)
        super(VersionsLogFileHandler, self).__init__(os.path.join(path, fName))