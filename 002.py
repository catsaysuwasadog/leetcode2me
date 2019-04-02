#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) CH, All rights reserved. Licensed by iduosi@icloud.com

# from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import time


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        n = 'null' if not self.next else self.next.val
        return ' [val=%s, next=%s] ' % (self.val, n)


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        h1 = l1
        h2 = l2
        l3 = ListNode(0)
        h3 = l3

        while h1 or h2 or h3:
            # print('start ---> ', h1, h2, h3)
            v = 0
            if h1:
                v += h1.val
                h1 = h1.next
            if h2:
                v += h2.val
                h2 = h2.next
            if h3:
                v += h3.val

            if v >= 10:
                h3.val = v % 10
                if h3.next:
                    print('h3 yes next ...')
                    h3.next.val += 1
                else:
                    print('h3 no next ...')
                    h3.next = ListNode(0)
                    h3.next.val += 1
                h3 = h3.next
            else:
                h3.val = v
                if h1 or h2:
                    if not h3.next:
                        h3.next = ListNode(0)
                h3 = h3.next
            # print('end ---< ', h1, h2, h3)
            # time.sleep(1)

        return l3


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)

nl1 = n1
n1.next = n2
n2.next = n3

n11 = ListNode(4)
n21 = ListNode(9)
n31 = ListNode(9)

nl2 = n11
n11.next = n21
n21.next = n31

print(nl1.val, nl1.next.val, nl1.next.next.val)
print(nl2.val, nl2.next.val, nl2.next.next.val)
nl = Solution().addTwoNumbers(nl1, nl2)
while nl:
    print(nl.val)
    nl = nl.next
