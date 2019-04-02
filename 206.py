#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) CH, All rights reserved. Licensed by iduosi@icloud.com

# from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        n = 'null' if not self.next else self.next.val
        return ' [val=%s, next=%s] ' % (self.val, n)


class Solution(object):
    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p, rev = head, None
        while p:
            print('+++', p, rev)
            # rev, rev.next, p = p, rev, p.next
            import copy
            oldrev = copy.deepcopy(rev)
            rev = copy.deepcopy(p)
            rev.next = oldrev
            p = p.next
            print('---', p, rev, rev.next)
            # rev = p
            # rev.next = rev

        return rev

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
            print('+++', curr, prev)
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)

nl = n1
n1.next = n2
n2.next = n3
print(nl.val, nl.next.val, nl.next.next.val)
nl = Solution().reverseList(n1)
print(nl.val, nl.next.val, nl.next.next.val)
