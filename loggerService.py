import os
import logging
import settings


# init log settings
def log_init():
    try:
        os.makedirs(settings.log_path)
        # set basic logger config
        logging.basicConfig(filename=str(settings.log_path) + 'service.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    except OSError:
        logging.info('Log dir ' + settings.log_path + ' is already exist')

    logging.info('PID:' + str(os.getpid()))
    logging.info('Log dir set to ' + settings.log_path)
