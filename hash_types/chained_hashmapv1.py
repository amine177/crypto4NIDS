#!/bin/env python
# -*- coding: utf-8 -*-


class Element:

    def __init__(self, e):
        self. e = e
        self.next = None

    def next(self):
        return self.next

    def __str__(self):
        return str(self.e)


def hash(e, f):
    return f(e)


def insertall(ls, hashmap, f):

    for i in ls:
        ie = Element(i)
        h = hash(ie.e, f)
        if hashmap[h] is not None:
            n = hashmap[h]
            while n.next is not None:
                n = n.next

            n.next = ie
        else:
            hashmap[h] = ie

    return hashmap


if __name__ == "__main__":

    hashmap = [None for i in range(11)]
    lst = [10, 22, 31, 4, 15, 28, 83, 88, 59, 37]

    hashmap = insertall(lst, hashmap, lambda x: x % 11)
    s = ""
    for i in hashmap:
        if i is not None:
            s = s + str(i)
            sui = i
            if sui.next is not None:
                s = s + "->" + str(sui.next) + ','
                while sui.next is not None:
                    sui = sui.next
                    if sui.next is None:
                        break
                    s = s + str(sui.next) + ","
            s += "|"
        else:
            s = s + "NULL" + "|"

    print("{}".format(s))
