# -*- coding:utf-8 -*-


# Reverse bits of a given 32 bits unsigned integer.
#
# Example:
#
#
# Input: 43261596
# Output: 964176192
# Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
#              return 964176192 represented in binary as 00111001011110000010100101000000.
#
#
# Follow up:
# If this function is called many times, how would you optimize it?
#


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        #自己写的，速度还不错，就是逻辑有点啰嗦，先转换成字符串，再转换成整数，有没有更好的方法？
        '''
        n = '%032d' % (int(bin(n)[2:]))
        return int(str(n)[::-1], base = 2)
        '''
        result = 0
        if n == 0: return result
        for _ in range(32):
            result <<= 1
            if (n & 1) == 1:
                result += 1
            n >>= 1
        return result
