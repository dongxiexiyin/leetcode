# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
#        自己写的，跟slide window的答案思路差不多，只不过自己用了list来控制每次取出的不重复的子数组，中间确定index的时候比较麻烦，用到了find，应该会遍历一下字符串，导致时间增加，提交的结果也说明了这一点
        resultList = []
        maxLen = curr = 0
        for i in range(len(s)):
            if s[i] in resultList:
                index = resultList.index(s[i])
                resultList = resultList[index + 1:]
                if maxLen < curr:
                    maxLen, curr = curr, len(resultList) + 1
                curr = len(resultList) + 1
            else:
                curr += 1
            resultList.append(s[i])
        return max(maxLen, curr)
        
        '''
        def AllUnique(s, i, j):
            resultSet = set([])
            for n in range(i, j):
                if s[n] in resultSet:
                    return False
                resultSet.add(s[n])
            return True
        
        ans = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if AllUnique(s, i, j):
                    ans = max(ans, j - i)
        return ans
        '''
        '''
        resultDict = {}
        maxLen = i = 0
        for j in range(len(s)):
            if s[j] in resultDict:
                i = max(resultDict.get(s[j]), i) #i的位置要固定在重复元素的下一个
            maxLen = max(maxLen, j - i + 1) #i代表实际位置的下一个，而j却代表实际位置，所以需要+1
            resultDict[s[j]] = j + 1 #把s[j]的位置固定在实际key的下一个，方便之后确定i的位置
        return maxLen
        '''
