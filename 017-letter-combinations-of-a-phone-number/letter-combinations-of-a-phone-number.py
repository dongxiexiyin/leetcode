# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#
#
# Example:
#
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
# Note:
#
# Although the above answer is in lexicographical order, your answer could be in any order you want.
#


from functools import reduce

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #自己写的，参考了map和reduce的用法，确实厉害
        if not digits: return []
        return list(self.digit2char(digits)) if len(digits) == 1 else reduce(self.combine, map(self.digit2char, digits))
    
    def digit2char(self, ch):
        digit2char = {'2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'}
        return digit2char[ch]
    
    def combine(self, s1, s2):
        return [x + y for x in s1 for y in s2]
