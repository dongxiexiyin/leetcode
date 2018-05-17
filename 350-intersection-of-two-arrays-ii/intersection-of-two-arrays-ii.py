#
# Given two arrays, write a function to compute their intersection.
#
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
#
#
# Note:
#
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
#
#
#
# Follow up:
#
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
#
#


from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #自己写的，用Counter类统计两个数组里每个元素出现的次数，然后做交集，得到在两个数组里每个共同元素出现的最少次数，然后加到result里
        '''
        resultList = []
        inter = Counter(nums1) & Counter(nums2)
        for key in inter:
            resultList.extend([key] * inter[key])
        return resultList
        '''
        #先排序再比较也可以
        resultList = []
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                resultList.append(nums1[i])
                i += 1
                j += 1
        return resultList
