#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def reducer():
    old_key = None
    student_list = []
    for line in sys.stdin:
        line = line.strip().split('\t')
        if len(line) == 2:
            current_key = line[0]
            student_id = line[1]
            if old_key and old_key != current_key:
                print '{0}\t{1}'.format(old_key, student_list)
                student_list = []
            old_key = current_key
            student_list.append(student_id)


reducer()