#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys

def reducer():
    hour_dict = {}
    old_user = None
    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(data) == 2:
            #print data
            current_user = data[0]
            hour = data[1]
            if old_user and old_user != current_user:
                do_comparision(hour_dict, old_user)
                hour_dict = {}
           
            old_user = current_user
            if hour_dict.has_key(hour) == False:
                hour_dict[hour] = 0  # initial count 0
            hr_count = hour_dict[hour]
            hr_count += 1
            hour_dict[hour] = hr_count
        else:
            continue
    do_comparision(hour_dict, old_user)  # for last hour entry
def do_comparision(hour_dict, old_user):
    hour_list = sorted(hour_dict, key=hour_dict.__getitem__, reverse=True)
    highest_hr = hour_list[0]
    print '{0}\t{1}'.format(old_user, highest_hr)
    if len(hour_list) > 0:
        for key in hour_list[1:]:
            if hour_dict[highest_hr] == hour_dict[key]:
                print '{0}\t{1}'.format(old_user, key)
            else:
                break
 


reducer()
