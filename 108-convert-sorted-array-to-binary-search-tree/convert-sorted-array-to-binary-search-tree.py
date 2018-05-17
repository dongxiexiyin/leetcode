# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example:
#
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        #自己写的
        return self.BST(nums, 0, len(nums))
    
    def BST(self, nums, p, q):
        if p >= q: return None
        mid = (p + q) // 2
        value = nums[mid]
        root = TreeNode(value)
        root.left = self.BST(nums, p, mid)
        root.right = self.BST(nums, mid + 1, q)
        return root
