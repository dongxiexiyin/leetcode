# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #自己写的，O(n2)的时间复杂度，超时
        '''
        maxArea = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                area = min(height[i], height[j]) * (j - i)
                if maxArea < area:
                    maxArea = area
        return maxArea
        '''
        #Solution 2，利用一前一后两个index来控制面积，每次移动较短的那一个index，因为面积的大小取决于短的那一个，所以移动短的可能会得到更大的面积，而移动长的则无济于事
        maxArea = 0
        i, j = 0, len(height) - 1
        while i < j:
            maxArea = max(maxArea, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea

