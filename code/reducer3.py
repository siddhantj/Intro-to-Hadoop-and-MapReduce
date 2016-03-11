#!/usr/bin/python
# -*- coding: utf-8 -*-

""" This is without the weighted score.
"""

import sys
import pdb


def reducer():
    key_count_collection = {}
    key_count = 0
    old_key = None
    for line in sys.stdin:
        line = line.split('\t')
        if len(line) == 2:
            current_key = line[0]
            if old_key and old_key != current_key:

                maintain_popular_tag(key_count_collection, old_key, key_count)
                key_count = 0
            old_key = current_key
            key_count += 1
    maintain_popular_tag(key_count_collection, old_key, key_count)
    keys = sorted(key_count_collection, key=key_count_collection.__getitem__,
                  reverse=True)
    for key in keys:
        print '{0}\t{1}'.format(key, key_count_collection[key])


def maintain_popular_tag(key_count_collection, old_key, key_count):
    """ Maintains a dictionary with top 10 popular tags. Priority Queue can
    be used too.
    :param key_count_collection: Dictionary containing tags and counts.
    :param old_key: The tag to be entered to dictionary
    :param key_count: Count of tag
    :return: None
    """
    if len(key_count_collection) == 10:
        ordered_tag_list = sorted(key_count_collection,
                                  key=key_count_collection.__getitem__)
        lowest_count = key_count_collection[ordered_tag_list[0]]
        if lowest_count < key_count:
            del key_count_collection[ordered_tag_list[0]]
            key_count_collection[old_key] = key_count
            # key_count = 0
        assert len(key_count_collection) is 10
    if len(key_count_collection) < 10:
        key_count_collection[old_key] = key_count

reducer()