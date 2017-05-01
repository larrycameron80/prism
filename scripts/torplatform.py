#! /usr/bin/env python

"""Fetch the Tor platform version for a given relay."""

import os
import sys
import json
import urllib2

LOG_FILE = os.path.join(os.path.expanduser('~'), 
                        '.tor', 'stats',
                        'bridge_passive_info.txt')
ONIONOO = "https://onionoo.torproject.org/details?search={0}"


def get_platform(ip):
    response = urllib2.urlopen(ONIONOO.format(ip))
    output = json.load(response)
    relays = output['relays']
    if not relays:
        return None
    platform = relays[0]['platform']
    return platform


def query_onionoo():
    ip_to_platform = {}
    with open(LOG_FILE) as f:
        next(f)
        for line in f:
            split_line = line.split('\t')
            ip_addr = split_line[1]
            if ip_addr == "NULL":
                ip_to_platform[ip_addr] = "NULL"
                continue

            platform = get_platform(ip_addr)
            if platform is None:
                platform = "None"

            ip_to_platform[ip_addr] = platform

    return ip_to_platform


def main():
    ip_addr_platform = query_onionoo()
    with open('platformoutput.txt', 'w') as f:
        for ip, platform in ip_addr_platform.iteritems():
            f.write('{0}\t{1}'.format(ip, platform))
            f.write('\n')


if __name__ == '__main__':
    if len(sys.argv) > 2:
        if sys.argv[1]:
            LOG_FILE = sys.argv[1]
    if not os.path.isfile(LOG_FILE):
        sys.exit('Log file not found.')

    main()
