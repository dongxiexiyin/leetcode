# -*- coding:utf-8 -*-


#
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
#
#
#
#
# Note: You may assume the string contain only lowercase letters.
#


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #自己写的，超时
        '''
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1
        '''
        #这个不超时，但是还是比较慢
        '''
        for i in range(len(s)):
            if s.index(s[i]) == s.rindex(s[i]):
                return i
        return -1
        '''
        #看了这么个鬼，据说打败了100%
        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
