#!/usr/bin/env python3
# HW08_ch11_ex02b
# This borrows from exercise two in the book.
# Dictionaries have a method called keys that returns the keys of the
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical
# order.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
###############################################################################
# Imports


# Body
def print_hist_old(h):
    h_key_sort = sorted(h.keys())
    for c in h_key_sort:
        print(c, h[c])
    # print(h_new)

# print_hist_old({'apple': 2, 'banana': 1, 'cherry': 10})

def print_hist_new(pledge):
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
def main():
    """ Calls print_hist_new with the appropriate arguments to print the
    histogram of pledge.txt.
    """
    pledge = histogram_new(get_pledge_list())
    print_hist_new(pledge)

if __name__ == '__main__':
    main()
