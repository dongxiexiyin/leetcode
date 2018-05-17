# -*- coding:utf-8 -*-


# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#
# Example:
#
#
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#              Since 2 has only one digit, return it.
#
#
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
#


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        #想了一下全是循环的方法，看了solution，除了0以外，其他数各位的和是1-9循环，所以addDigits(n) = addDigits(n - 9) (n > 9)，所以只要把任何数转化成9以内的数即可
        return 1 + (num - 1) % 9 if num > 0 else 0
