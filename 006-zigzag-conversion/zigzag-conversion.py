# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
#
# string convert(string s, int numRows);
#
# Example 1:
#
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
#
# Example 2:
#
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #自己写的，应该是O(n2)吧
        if numRows == 1:
            return s
        totalLens = 2 * numRows - 2
        lpad = len(s) % totalLens
        if lpad != 0:
            s += '#' * (totalLens - lpad)
        resultRow = len(s) // totalLens
        resultStr = ''
        i, j = 1, totalLens - 1
        for k in range(resultRow):
    	    resultStr += s[k * totalLens]
        while i < j:
    	    for k in range(resultRow):
    		    resultStr += s[k * totalLens + i]
    		    resultStr += s[k * totalLens + j]
    	    i += 1
    	    j -= 1
        for k in range(resultRow):
            resultStr += s[k * totalLens + totalLens // 2]
        resultStr = resultStr.replace('#', '')
        return resultStr
