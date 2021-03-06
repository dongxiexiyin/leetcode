# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
#
# 	I can be placed before V (5) and X (10) to make 4 and 9. 
# 	X can be placed before L (50) and C (100) to make 40 and 90. 
# 	C can be placed before D (500) and M (1000) to make 400 and 900.
#
#
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
#
# Example 1:
#
#
# Input: "III"
# Output: 3
#
# Example 2:
#
#
# Input: "IV"
# Output: 4
#
# Example 3:
#
#
# Input: "IX"
# Output: 9
#
# Example 4:
#
#
# Input: "LVIII"
# Output: 58
# Explanation: C = 100, L = 50, XXX = 30 and III = 3.
#
#
# Example 5:
#
#
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        #自己写的
        resultList = []
        result = 0
        for i in range(len(s)):
            if s[i] == 'M': resultList.append(1000)
            elif s[i] == 'D': resultList.append(500)
            elif s[i] == 'C': resultList.append(100)
            elif s[i] == 'L': resultList.append(50)
            elif s[i] == 'X': resultList.append(10)
            elif s[i] == 'V': resultList.append(5)
            elif s[i] == 'I': resultList.append(1)
        for i in range(len(resultList) - 1):
            if resultList[i] < resultList[i + 1]:
                resultList[i] = -resultList[i]
        for i in range(len(resultList)):
            result += resultList[i]
        return result
        '''
        l = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        result = 0
        for i in range(len(s)):
            result += l[s[i]]
            if i > 0 and l[s[i-1]] < l[s[i]]:
                result -= l[s[i-1]]*2
        return result
