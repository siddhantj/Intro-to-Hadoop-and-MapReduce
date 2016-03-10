#!/usr/bin/python
#-*- coding: utf-8 -*-

from datetime import datetime
import csv
import sys
import pdb

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    reader.next()
    try:
        for line in reader:
            #print line[0]         
            student_id = line[3]
            datetime_str = line[8]
            datetime_str = datetime_str.strip('0')
            datetime_str = datetime_str.strip('+')
            datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S.%f')
            #hour = datetime_obj.hour
            print '{0}\t{1}'.format(student_id, datetime_obj.hour)


    except:
        pass



mapper()
