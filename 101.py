#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) CH, All rights reserved. Licensed by iduosi@icloud.com

# from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def _isSymmetric(self, p, q):
        """
        :param p:
        :param q:
        :return:
        """
        if not p and not q:
            return True

        if not (p and q):
            return False

        if p.val != q.val:
            return False

        return self._isSymmetric(p.left, q.right) and self._isSymmetric(p.right, q.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self._isSymmetric(root.left, root.right)


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(2)
n4 = TreeNode(3)
n5 = TreeNode(4)
n6 = TreeNode(4)
n7 = TreeNode(4)

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


print(Solution().isSymmetric(n1))
