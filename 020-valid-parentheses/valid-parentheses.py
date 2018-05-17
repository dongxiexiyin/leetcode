# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# 	Open brackets must be closed by the same type of brackets.
# 	Open brackets must be closed in the correct order.
#
#
# Note that an empty string is also considered valid.
#
# Example 1:
#
#
# Input: "()"
# Output: true
#
#
# Example 2:
#
#
# Input: "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: "{[]}"
# Output: true
#
#


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        #这个思路很好，将成对的括号去掉，如果嵌套正确最终的字符串应该为空，但是时间复杂度比较高，尝试用栈的思路解决一下
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
        return s == ''
        '''
        resultList = []
        for ch in s:
            if ch == '(': resultList.append(')')
            elif ch == '[': resultList.append(']')
            elif ch == '{': resultList.append('}')
            elif len(resultList) == 0 or resultList.pop() != ch: return False
        return len(resultList) == 0
