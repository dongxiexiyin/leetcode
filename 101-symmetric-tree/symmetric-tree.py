# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
#
# But the following [1,2,2,null,3,null,3]  is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
#
#
#
# Note:
# Bonus points if you could solve it both recursively and iteratively.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)
    
    def isMirror(self, p, q):
        if p is None and q is None: return True
        if p is None or q is None: return False
        return p.val == q.val and self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)
