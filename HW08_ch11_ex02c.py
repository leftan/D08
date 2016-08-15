#!/usr/bin/env python3
# HW08_ch11_ex02c.py
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
###############################################################################
# Imports

# d = {'a': 1, 'b': 0, 'c': 1}

# Body
def reverse_lookup_old(d, v):
    result = []
    for k, val in d.items():
        if val == v:
            result.append(k)
    raise ValueError
    return result

# print(reverse_lookup_old(d, 1))

def reverse_lookup_new(pledge, v):
    result = []
    for k, val in pledge.items():
        if val == v:
            result.append(k)
    return result


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

def main():   # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    # print(pledge_histogram)
    print(reverse_lookup_new(pledge_histogram, 1))
    print(reverse_lookup_new(pledge_histogram, 9))
    print(reverse_lookup_new(pledge_histogram, "Python"))

if __name__ == '__main__':
    main()
