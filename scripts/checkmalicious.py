#! /usr/bin/env python

EXONERATOR = "results-sorted.txt"
EXONERATOR_OUTPUT = "exonerator.txt"
COMMAND = "whois {0}"

import shlex
import subprocess


def main():
    ip = []
    with open(EXONERATOR) as f:
        for line in f:
            ip.append(line.strip())

    ip_to_country = {}
    for each in ip:
        output = subprocess.Popen(shlex.split(COMMAND.format(each)),
                                  stdout=subprocess.PIPE)
        out = output.communicate()[0].splitlines()
        run_once = False
        for _ in out:
            if _.startswith('country'):
                ip_to_country[each] = _.split(':')[-1].upper()
                run_once = True
        if not run_once:
            ip_to_country[each] = "?"

    with open(EXONERATOR_OUTPUT, 'w') as f:
        for a, b in ip_to_country.iteritems():
            f.write('{0}\t{1}'.format(a, b))
            f.write('\n')


if __name__ == "__main__":
    main()
