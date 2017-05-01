#! /usr/bin/env python

"""Fetch all logs. From all machines."""

import os
import sys
import shlex
import subprocess
import ConfigParser

CONFIG_FILE = os.path.join(os.path.expanduser('~'),
                           'logs.cfg')
SSH_COMMAND = "scp -i {0} {1}:~/.tor/stats/bridge_passive_info.txt {2}"
LOG_FILE = 'all-logs.log'

def read_config():
    machines = {}

    config = ConfigParser.SafeConfigParser()
    config.read(CONFIG_FILE)
    for section in config.sections():
        key = config.get(section, 'key')
        ip = config.get(section, 'ip')
        machines[section] = (key, ip)

    return machines


def fetch_all_logs():
    machines = read_config()
    for machine, values in machines.iteritems():
        if not os.path.isfile(values[0]):
            sys.exit("Not a valid file: {0}".format(values[0]))

        print 'Fetching file from {0}...'.format(machine)
        subprocess.call(shlex.split(SSH_COMMAND.format(values[0],
                                                       values[1],
                                                       machine)))

    log_files = machines.keys()
    open(LOG_FILE, 'w').close()

    for each in log_files:
        with open(each) as f:
            with open(LOG_FILE, 'a') as l:
                l.write(f.read())
        os.remove(each)

if __name__ == '__main__':
    fetch_all_logs()
