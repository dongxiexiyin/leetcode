# -*- coding:utf-8 -*-


#
# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom 
# note can be constructed from the magazines ; otherwise, it will return false. 
#
#
# Each letter in the magazine string can only be used once in your ransom note.
#
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
#
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
#
#


from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #自己写的，有点慢？
        '''
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)
        return c1 | c2 == c2
        '''
        for ch in ransomNote:
            if ch in magazine:
                magazine = magazine.replace(ch, '', 1)
            else:
                return False
        return True
