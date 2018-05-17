# -*- coding:utf-8 -*-


# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
#
# Input: s = "anagram", t = "nagaram"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "rat", t = "car"
# Output: false
#
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
#


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #自己写的，用counter类统计两个字符串中字母出现的次数，如果相等就是anagram
        '''
        return collections.Counter(s) == collections.Counter(t)
        '''
        #用dict行不行？
        resultDict = {}
        for ch in s:
            if ch in resultDict:
                resultDict[ch] += 1
            else:
                resultDict[ch] = 1
        for ch in t:
            if ch in resultDict:
                resultDict[ch] -= 1
            else:
                return False
        for n in resultDict.values():
            if n != 0: return False
        return True
