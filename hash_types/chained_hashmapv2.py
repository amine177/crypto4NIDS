# !/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict


def hash_mod(n, m):
    return n % m


def insert(hashmap, e, n):

    hashmap[hash_mod(e, n)].append(e)
    return hash_mod(e, n) + hashmap[hash_mod(e, n)].index(e)


if __name__ == "__main__":

    lst = [10, 22, 31, 4, 15, 28, 83, 88, 59, 37]
    hashmap = defaultdict(list)

    for e in lst:
        print("insert", e, "at", insert(hashmap, e, 11))

    print(hashmap)
