# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root, isT = False):
        """
        :type root: TreeNode
        :rtype: int
        """
        #自己写的，搞清楚如何判断一个节点是左叶节点就好办了
        '''
        if root is None: return 0
        if root.left is not None and root.left.left is None and root.left.right is None: return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        '''
        #看见一个solution，有点意思，给函数加了一个默认参数isT，默认值为False
        if root is not None and isT and root.left is None and root.right is None: return root.val
        else:
            return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right) if root is not None else 0
