# -*- coding:utf-8 -*-


# We are playing the Guess Game. The game is as follows: 
#
# I pick a number from 1 to n. You have to guess which number I picked.
#
# Every time you guess wrong, I'll tell you whether the number is higher or lower.
#
# You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
#
# -1 : My number is lower
#  1 : My number is higher
#  0 : Congrats! You got it!
#
#
# Example:
#
# n = 10, I pick 6.
#
# Return 6.
#
#


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        #二分查找，就爱玩个文字游戏
        low, high = 1, n
        while low <= high:
            mid = low + (high - low) // 2
            if guess(mid) == 1:
                low = mid + 1
            elif guess(mid) == -1:
                high = mid
            else:
                return mid
        return -1
