#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) CH, All rights reserved. Licensed by iduosi@icloud.com

# from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x > 0:
            x_s = str(x)
            x_s = x_s[::-1]
        else:
            x_s = str(x)
            x_s = x_s[0] + x_s[1:][::-1]
        x_i = int(x_s)
        if x_i > 2**31-1 or x_i < -2**31:
            x_i = 0
        return x_i


print(Solution().reverse(0))
print(Solution().reverse(1234556))
print(Solution().reverse(2147483649))
print(Solution().reverse(-321))
