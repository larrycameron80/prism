#! /usr/bin/env python

import os
import sys
import shlex
import subprocess

import numpy as np
import matplotlib.pyplot as plt

from fetchlogs import LOG_FILE

COUNTRY = "country.dat"
READYOPEN = "readyopen.dat"
TOTALRELAY = "totalrelay.dat"
TOTALTIME = "time.dat"


def countries():
    countries_lst = []
    with open(COUNTRY) as f:
        for line in f:
            country, freq = line.strip().split()
            if country == "??":
                country = "?"
            countries_lst.append((country, int(freq)))

    N = len(countries_lst)
    x = np.arange(1, N+1)
    y = [num for (s, num) in countries_lst]
    labels = [s for (s, num) in countries_lst]
    plt.rcParams['xtick.major.pad']= '12'
    width = .5
    plt.bar(x, y, width, color='b')
    plt.ylabel('Visits')
    plt.xlabel('Country')
    plt.title('Visits from Different Countries')
    plt.xticks(x + width/2.0, labels, rotation='horizontal', va='baseline')
    plt.savefig("country.png")
    plt.clf()


def ready_open():
    ready_open = []
    with open(READYOPEN) as f:
        for line in f:
            state, freq = line.strip().split()
            ready_open.append((state, int(freq)))

    N = len(ready_open)
    x = np.arange(1, N+1)
    y = [num for (s, num) in ready_open]
    labels = [s for (s, num) in ready_open]
    width = .5
    plt.bar(x, y, width, color='b')
    plt.ylabel('Count')
    plt.xlabel('Connection State')
    plt.title('ReadyOpen Connections')
    plt.xticks(x + width/2.0, labels)
    plt.savefig("readyopen.png")
    plt.clf()


def total_relay():
    total_relay = []
    with open(TOTALRELAY) as f:
        for line in f:
            state, freq = line.strip().split()
            total_relay.append((state, int(freq)))

    N = len(total_relay)
    x = np.arange(1, N+1)
    y = [num for (s, num) in total_relay]
    labels = [s for (s, num) in total_relay]
    width = .5
    plt.bar(x, y, width, color='b')
    plt.ylabel('Count')
    plt.xlabel('Cells Relayed')
    plt.title('Total Cells Relayed')
    plt.xticks(x + width/2.0, labels)
    plt.savefig("totalrelayed.png")
    plt.clf()


def total_time():
    total_time = []
    with open(TOTALTIME) as f:
        for line in f:
            state, freq = line.strip().split()
            total_time.append((state, int(freq)))

    N = len(total_time)
    x = np.arange(1, N+1)
    y = [num for (s, num) in total_time]
    labels = [s for (s, num) in total_time]
    width = .5
    plt.bar(x, y, width, color='b')
    plt.ylabel('Count')
    plt.xlabel('Connection Duration')
    plt.title('Total Time of Connections')
    plt.xticks(x + width/2.0, labels)
    plt.savefig("totaltime.png")
    plt.clf()


def main():
    # Countries.
    print 'Generating countries graph...'
    countries()

    # ReadyOpen.
    print 'Generating ReadyOpen...'
    ready_open()

    # TotalCreateCells.
    print 'Generating total relay cells...'
    total_relay()

    # Time.
    print 'Generating total time...'
    total_time()


if __name__ == "__main__":
    main()
