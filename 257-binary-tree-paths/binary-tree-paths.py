# -*- coding:utf-8 -*-


# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
#
# Input:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None: return []
        return self.binaryTreePathsRec(root, '').replace(':', '->').split(',')
    
    def binaryTreePathsRec(self, root, s):
        if root.left is None and root.right is None: return s + str(root.val)
        elif root.left is None: return self.binaryTreePathsRec(root.right, s + str(root.val) + ':')
        elif root.right is None: return self.binaryTreePathsRec(root.left, s + str(root.val) + ':')
        else: return self.binaryTreePathsRec(root.left, s + str(root.val) + ':') + ',' + self.binaryTreePathsRec(root.right, s + str(root.val) + ':')
