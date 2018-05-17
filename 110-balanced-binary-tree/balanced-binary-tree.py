# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
#
# a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
#
# Example 1:
#
# Given the following tree [3,9,20,null,null,15,7]:
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# Return true.
#
# Example 2:
#
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
#
#
# Return false.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        '''
        #自己写的
        if root is None: return True #平衡二叉树可以是空树
        diff = self.depth(root.left) - self.depth(root.right)
        if diff > 1 or diff < -1: #如果自己的左右两棵树的深度相差超过1，则不是平衡二叉树
            return False
        else: #如果自己的左右两棵树的深度相差不超过1，那么还要继续看左右两棵子树各自是不是平衡二叉树
            return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def depth(self, t):
        return 1 + max(self.depth(t.left), self.depth(t.right)) if t is not None else 0
        '''
        #看了一个solution，应该比我的快，我写的重复计算了很多次深度，这个写法如果返回-1，就不计算深度，一直把-1往上返回，如果不等于-1，那么计算当前节点的深度
        ans= self.isB(root)
        if ans is not -1:
            return True
        else:
            return False
            
    def isB(self, root):
        if root == None:
            return 0
        leftH = self.isB(root.left)
        if leftH == -1:
            return -1
        rightH = self.isB(root.right)
        if rightH == -1:
            return -1
        if abs(leftH - rightH) > 1:
            return -1
        return 1 + max(rightH, leftH)
