# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
#
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
#
# The matching should cover the entire input string (not partial).
#
# Note:
#
#
# 	s could be empty and contains only lowercase letters a-z.
# 	p could be empty and contains only lowercase letters a-z, and characters like . or *.
#
#
# Example 1:
#
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
# Example 2:
#
#
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
#
#
# Example 3:
#
#
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#
#
# Example 4:
#
#
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
#
#
# Example 5:
#
#
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
#
#


import re

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #自己写的，有re模块就是好
        '''
        return True if re.match('^' + p + '$', s) else False
        '''
        #Solution 1，如果不让用re模块，需要自己写匹配函数，那么我们分两种情况，第一种是不带*的，第二种是带*的。不带*的很简单，只要依次匹配s和p中的每一个字符就行了
        #if not pattern: return not text
        #first_match = bool(text) and pattern[0] in {text[0], '.'}
        #return first_match and isMatch(text[1:], pattern[1:])
        #带*的会稍微复杂一点，如果p中有*，那么他一定在p[1]，这种情况下我们要不忽略这一部分pattern，要不跳过字符串中匹配的那个字符。如果剩余的字符串都能通过这样的匹配，那么返回True
        '''
        if not p: return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])
        '''
        #Solution 2, Dynamic Programming，用一个dict保存中间计算的结果
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)
                memo[i, j] = ans
            return memo[i, j]
        return dp(0, 0)
        
        
