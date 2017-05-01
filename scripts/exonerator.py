#! /usr/bin/env python

"""Query the ExoneraTor service to check if an address is a Tor relay or not."""

import os
import sys
import urllib2
import datetime

from BeautifulSoup import BeautifulSoup as BS

from fetchlogs import LOG_FILE

EXONERATOR = ("https://metrics.torproject.org/exonerator.html?"
              "targetaddr=&targetPort=&ip={0}&timestamp={1}#relay")


def unix_time_to_date(time):
    date = datetime.datetime.fromtimestamp(int(time))
    formatted_date = date.strftime("%Y-%m-%d")
    return formatted_date


def read_log_file():
    ip_to_date = []
    with open(LOG_FILE) as f:
        for line in f:
            split_line = line.split('\t')
            ip_addr = split_line[1]
            unix_time = int(split_line[2])

            date = unix_time_to_date(unix_time)
            ip_to_date.append((ip_addr, date))
    
    return ip_to_date


def main():
    data = read_log_file()
    ip = [i for (i, d) in data]
    date = [d for (i, d) in data]

    f = open('results.txt', 'w')
    for i, d in zip(ip, date):
        soup = BS(urllib2.urlopen(EXONERATOR.format(i, d)).read())
        all_p = soup.findAll('p')
        # The fifth paragraph from the end.
        result = all_p[-5].renderContents()
        if 'NEGATIVE' in result:
            f.write(i)
            f.write('\n')
            f.flush()

    f.close()
    sys.exit()


if __name__ == '__main__':
    main()
