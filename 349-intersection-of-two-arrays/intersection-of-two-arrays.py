#
# Given two arrays, write a function to compute their intersection.
#
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
#
#
# Note:
#
# Each element in the result must be unique.
# The result can be in any order.
#
#


class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #brute force，循环看nums1里的元素是否出现在nums2里，如果有，就return，时间复杂度O(n2)
        #自己写的，既然与顺序无关，那么就可以用set和它的&特性了
        return list(set(nums1) & set(nums2))
