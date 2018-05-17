#
#     Given an integer, write a function to determine if it is a power of three.
#
#
#     Follow up:
#     Could you do it without using any loop / recursion?
#
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases.


class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #approach 1，循环判断
        #approach 2，转换为三进制，然后判断是否只包含一个1，Java可以用Integer.toString(5, 3) = '12'，但是python没有相关的方法
        #approach 3，用数学公式，n = 3^i, i = log3(n) = logb(n) / logb(3)，当n是3的幂次时，i一定为整数，所以用i % 1 == 0来判断是否为整数
        '''
        epsilon = 0.000000000001
        return (math.log(n) / math.log(3) + epsilon) % 1 <= 2 * epsilon if n >= 1 else False
        '''
        #approach 4，在一些会产生整数溢出的语言当中，正整数的最大值为2147483647，那么3的幂次的最大值为1162261467，所以如果n > 0且1162261467 % n == 0的话，n为3的幂次
        return n > 0 and 1162261467 % n == 0
        #approach 4其实可以用来计算任何质数的幂次，合数不行
