# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
# Each LED represents a zero or one, with the least significant bit on the right.
#
# For example, the above binary watch reads "3:25".
#
# Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.
#
# Example:
# Input: n = 1Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
#
#
# Note:
#
# The order of output does not matter.
# The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
# The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
#
#


class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        #自己没想出来，想的有点复杂，其实很简单，既然是binary watch，那一定跟位运算有关，给定了num，用两个循环嵌套，如果此时的时和分所包含1的个数相加等于num，那么就把结果append到list里
        resultList = []
        for i in range(12):
            for j in range(60):
                if self.getBit(i) + self.getBit(j) == num:
                    resultList.append('%d:%02d' % (i, j))
        return resultList
    
    def getBit(self, num):
        count = 0
        while num != 0:
            num &= (num - 1)
            count += 1
        return count
            
