import os
import configparser


# get settings from file

conf = configparser.ConfigParser()
conf.read('settings.ini')

purge_path = conf['purgedir']['purge_path']

log_path = conf['logdir']['log_path']

# create setting file if not exist
def createSettingsFile():
    if not os.path.exists('settings.ini'):
        file = open('settings.ini', 'w+')
        file.write(
'''[purgedir]purge_path=/tmp/var/testdir/

[logdir]
log_path=/tmp/log/daemon/''')
        file.close()