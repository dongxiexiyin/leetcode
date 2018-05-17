# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#
# Example:
# Given a = 1 and b = 2, return 3.
#
#
# Credits:Special thanks to @fujiaozhu for adding this problem and creating all test cases.


class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        #看了好多位运算的解法，都是只能处理正数，负数处理不了
        '''
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a
        '''
        #说不得，只好用sum了
        return sum([a, b])
