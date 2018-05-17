# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
#
# Example 1:
#
#
# Input: s = "egg", t = "add"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "foo", t = "bar"
# Output: false
#
# Example 3:
#
#
# Input: s = "paper", t = "title"
# Output: true
#
# Note:
# You may assume both s and t have the same length.
#


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #自己写的，时间上还不错，就是空间上不太好。。
        '''
        dictS, dictT = {}, {}
        listS, listT = [], []
        for i in range(len(s)):
            if s[i] in dictS:
                listS.append(dictS[s[i]])
            else:
                dictS[s[i]] = i
                listS.append(i)
            if t[i] in dictT:
                listT.append(dictT[t[i]])
            else:
                dictT[t[i]] = i
                listT.append(i)
        return listS == listT
        '''
        #看了一个solution，核心思想差不多，但是只用了一个dict，很好
        resultDict = {}
        for i in range(len(s)):
            if s[i] not in resultDict:
                if t[i] in resultDict.values():
                    return False
                resultDict[s[i]] = t[i]
            elif resultDict[s[i]] != t[i]:
                return False
        return True
    
