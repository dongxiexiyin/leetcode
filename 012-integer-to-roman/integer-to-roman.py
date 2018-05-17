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
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
#
# Example 1:
#
#
# Input: 3
# Output: "III"
#
# Example 2:
#
#
# Input: 4
# Output: "IV"
#
# Example 3:
#
#
# Input: 9
# Output: "IX"
#
# Example 4:
#
#
# Input: 58
# Output: "LVIII"
# Explanation: C = 100, L = 50, XXX = 30 and III = 3.
#
#
# Example 5:
#
#
# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #自己写的
        '''
        DIGITS = {1 : 'I', 5 : 'V', 10 : 'X', 50 : 'L', 100 : 'C', 500 : 'D', 1000 : 'M', 4 : 'IV', 9 : 'IX', 40 : 'XL', 90 : 'XC', 400 : 'CD', 900 : 'CM'}
        radix = 1
        resultList = []
        while num != 0:
            number = num % 10 * radix
            if number in DIGITS:
                resultList.append(DIGITS[number])
            else:
                digit = number // radix
                if digit < 5:
                    resultList.append(DIGITS[radix] * digit)
                else:
                    resultList.append(DIGITS[5 * radix] + DIGITS[radix] * (digit - 5))
            num //= 10
            radix *= 10
        return ''.join(resultList[::-1])
        '''
        #看了一个Solution，用两个list分别保存罗马数字和对应的阿拉伯数字，每次减去一部分，直到num = 0
        digitsRoman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        digits = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        resultStr = ''
        i = 0
        while num > 0:
            if num - digits[i] >= 0:
                resultStr += digitsRoman[i]
                num -= digits[i]
            else:
                i += 1
        return resultStr
