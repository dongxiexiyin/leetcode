# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
#
# Input: ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Note:
#
# All given inputs are in lowercase letters a-z.
#


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        '''
        #自己写的，先找到最短的串，然后依次匹配
        if len(strs) == 0: return ''
        minStr, index = len(strs[0]), 0
        maxPrefix = ''
        for i in range(len(strs)):
            if minStr > len(strs[i]):
                minStr = len(strs[i])
                index = i

        flag = 1
        for i in range(minStr):
            for j in range(len(strs)):
                currStr = strs[index][:i + 1]
                if strs[j].find(currStr) != 0:
                    flag = -1
                    break
            if flag == 1 and len(currStr) > len(maxPrefix):
                maxPrefix = currStr
            elif flag == -1:
                return maxPrefix
        return maxPrefix
        '''
        '''
        #Vertical scanning
        if strs == None or len(strs) == 0: return ''
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0]
        '''
        #Horizontal scanning
        if strs == None or len(strs) == 0: return ''
        prefix = strs[0]
        for i in range(len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:len(prefix) - 1]
                if len(prefix) == 0: return ''
        return prefix
                        
