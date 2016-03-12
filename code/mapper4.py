#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import sys


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        if len(line) == 19:
            node_type = line[5]
            if node_type == 'question': # This is a question
                node_id = line[0]
                student_id = line[3]
                print '{0}\t{1}'.format(node_id, student_id)
            else:  # Check if this answer or comment has question
                parent_node_id = line[6]
                student_id = line[3]
                print '{0}\t{1}'.format(parent_node_id, student_id)

mapper()