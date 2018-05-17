# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
#
# Note: Do not use any built-in library function such as sqrt.
#
#
# Example 1:
#
# Input: 16
# Returns: True
#
#
#
# Example 2:
#
# Input: 14
# Returns: False
#
#
#
# Credits:Special thanks to @elmirap for adding this problem and creating all test cases.


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #自己写的，简单粗暴，效率不高
        '''
        i = 0
        while True:
            if i * i == num:
                return True
            elif i * i < num:
                i += 1
            else:
                return False
        '''
        #数学公式，所有的完全平方数都可以被表示成奇数和
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0
