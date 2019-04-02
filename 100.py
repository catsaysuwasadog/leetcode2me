#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) CH, All rights reserved. Licensed by iduosi@icloud.com

from __future__ import absolute_import
# from __future__ import division
# from __future__ import print_function
from __future__ import unicode_literals


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


class Solution(object):
    def isSameTree2(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True

        if not (p and q):
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self._trans(p) == self._trans(q)

    def _trans(self, p, rl=None):
        """
        :param p: TreeNode
        :return: list
        """
        if rl is None:
            rl = []
        if p:
            rl.append(p.val)
        else:
            return rl

        if p.right is None and p.left is None:
            return rl

        if p.left is not None:
            self._trans(p.left, rl)
        else:
            rl.append(None)

        if p.right is not None:
            self._trans(p.right, rl)
        else:
            rl.append(None)
        return rl


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(2)
n4 = TreeNode(3)
n5 = TreeNode(4)
n6 = TreeNode(4)
n7 = TreeNode(3)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
#      1
#     /  \
#    2    2
#   /\    /\
#  3  4  4  3


print(Solution()._trans(n1))

print(Solution().isSameTree2(n1, n1))
