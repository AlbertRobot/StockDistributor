# -*- coding: utf-8 -*-
import getopt
import sys

CONF_FILE = '../app.conf'
DATA_FILE = '../testdata.csv'


def parse():
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
    for op, value in opts:
        if op == "-c":
            CONF_FILE = value
        elif op == "-d":
            DATA_FILE = value

