# -*- coding:utf-8 -*-


# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
#     ...
#
#
# Example 1:
#
#
# Input: 1
# Output: "A"
#
#
# Example 2:
#
#
# Input: 28
# Output: "AB"
#
#
# Example 3:
#
#
# Input: 701
# Output: "ZY"
#
#


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        #自己写的
        resultStr = ''
        while n != 0:
            n = n - 1
            resultStr += chr(n % 26 + 65)
            n //= 26
        return resultStr[-1:-len(resultStr) - 1:-1]
