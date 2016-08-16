#!/usr/bin/env python3
# HW08_ch11_ex02d.py
# (1) Write a more concise version of invert_dict_old.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Update print_hist_new from HW08_ch11_ex02b.py to be able to print
# a sorted version of the dict (print key/value pairs from 0 through the
# largest key values, (and those in between))
# Ex. If d = {1:["this, that"], 3: ["the"]}, it prints:
#    '1: ["this", "that"]'
#    '2:'
#    '3: ["the"]'
###############################################################################
# Imports


# Body

def invert_dict_old(d):
    inverse = dict()
    for key, val in d.items():
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def invert_dict_new(pledge):
    inverse = dict()
    for key, val in pledge.items():
        inverse[val] = inverse.get(val, [])
        inverse[val].append(key)
        # if val not in inverse:
        #     inverse[val] = [key]
        # else:
        #     inverse[val].append(key)
    return inverse



def print_hist_newest(pledge):
    pledge_keys = pledge.keys()
    pledge_sort = sorted(pledge_keys)
    for word in pledge_sort:
        print(word, pledge[word])


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def histogram_old(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def histogram_new(pledge):
    d = dict()
    pledge = get_pledge_list()
    for word in pledge:
        d[word] = d.get(word, 0) + 1
    return d


def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. returns the list.
    """
    pledge_list = []
    with open('pledge.txt', 'r') as fin:
        for line in fin:
            pledge_list += line.split()
    return pledge_list

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():  # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    pledge_invert = invert_dict_new(pledge_histogram)
    print_hist_newest(pledge_invert)

if __name__ == '__main__':
    main()
