#
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
#
# Example:
# Given num = 16, return true.
# Given num = 5, return false.
#
#
# Follow up: Could you solve it without loops/recursion?
#
# Credits:Special thanks to @yukuairoy  for adding this problem and creating all test cases.


class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #自己写的，还是老方法，转换为字符串，然后判断1的个数并且判断1后面有多少个0
        '''
        resultStr = bin(num)
        return resultStr.count('1') == 1 and (len(resultStr) - resultStr.index('1') - 1) % 2 == 0 if num >= 1 else False
        '''
        #看了一个solution，在n & (n - 1) == 0上再加一个条件(n - 1) % 3 == 0
        return num > 0 and num & (num - 1) == 0 and (num - 1) % 3 == 0
