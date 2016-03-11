#!/usr/bin/python
# -*- coding: utf-8 -*-

""" This is without any weighted score.
"""
import csv
import sys


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    reader.next()
    for line in reader:
        if len(line) == 19:
            node_type = line[5]
            if node_type == 'question':
                tag_list = line[2].split(' ')
                for tag in tag_list:
                    print '{0}\t1'.format(tag)
            else:
                continue

mapper()