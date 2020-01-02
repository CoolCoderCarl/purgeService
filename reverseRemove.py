import os
import shutil
import logging

import settings


# remove all content from dir
def remove_dir():
    try:
        logging.info('Purge dir set to ' + settings.purge_path)
        # make path understandable for host system
        path_for_remove = os.path.join(os.path.abspath(os.path.dirname(__file__)), settings.purge_path)
        # if path exist - remove files
        if os.path.exists(path_for_remove):
            shutil.rmtree(path_for_remove)
            logging.critical('All files was removed from ' + settings.purge_path)
        # else - create path
        else:
            os.makedirs(path_for_remove)
            logging.info(path_for_remove + ' was created')
    except FileNotFoundError:
        logging.exception('Files in ' + settings.purge_path + ' not exist')