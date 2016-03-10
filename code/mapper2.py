#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import sys


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    reader.next()
    for line in reader:
        if len(line) == 19:
            id = line[0]
            body = line[4]
            post_type = line[5]
            parent_id = line[6]
            if post_type == 'question':
                print '{0}\t{1}\t{2}'.format(id, post_type, len(body))
            elif post_type == 'answer':
                # parent_id must be question
                print '{0}\t{1}\t{2}'.format(parent_id, post_type, len(body))
            else:
                # Comments and others
                continue
        else:
            continue

mapper()
