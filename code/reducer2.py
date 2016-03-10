#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def reducer():
    answer_len = 0
    answer_count = 0
    ques_len = 0
    old_id = None
    for line in sys.stdin:
        data = line.strip().split('\t')
        current_id, post_type, post_len = data
        if old_id and old_id != current_id:
            do_comparison(old_id, ques_len, answer_len, answer_count)
            ques_len = 0
            answer_len = 0
            answer_count = 0
        old_id = current_id
        if post_type == 'question':
            ques_len += int(post_len)
        elif post_type == 'answer':
            answer_len += int(post_len)
            answer_count += 1
        else:
            continue
    # last entry
    do_comparison(old_id, ques_len, answer_len, answer_count)


def do_comparison(old_id, ques_len, answer_len, answer_count):
    if answer_count != 0:
        avg_ans = float(answer_len/answer_count)
    else:
        avg_ans = 0
    print '{0}\t{1}\t{2}'.format(old_id, ques_len, avg_ans)


reducer()
