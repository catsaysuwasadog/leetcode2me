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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        pass

    def _looptree(self, n, c=0):
        """
        :param n:
        :return:
        """
        if not n:
            return 0

        if not n.left and not n.right:
            return c + 1




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
