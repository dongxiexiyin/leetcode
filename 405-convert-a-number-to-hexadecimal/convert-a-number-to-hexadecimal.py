#
# Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.
#
#
# Note:
#
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed integer.
# You must not use any method provided by the library which converts/formats the number to hex directly.
#
#
#
# Example 1:
#
# Input:
# 26
#
# Output:
# "1a"
#
#
#
# Example 2:
#
# Input:
# -1
#
# Output:
# "ffffffff"
#
#


class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        #自己写的，搞一个dict存放16进制对应的值，判断num的正负，确定num的最终值，然后反复%16
        #给的twos_complement函数有点奇怪，比如-1返回的是-4294967297，-2返回-4294967298，所以只能取绝对值之后再+2*num，得到想要的正值
        if num == 0: return '0'
        hexDict = {0: '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9', 10 : 'a', 11 : 'b', 12 : 'c', 13 : 'd', 14 : 'e', 15 : 'f'}
        resultStr = ''
        if num < 0:
            num = abs(self.twos_complement(num, 32)) + 2 * num
        while num != 0:
            resultStr += hexDict[num % 16]
            num //= 16
        return resultStr[::-1]
    
    def twos_complement(self, input_value, num_bits):
	    mask = 2 ** (num_bits - 1)
	    return -(input_value & mask) + (input_value & ~mask)
