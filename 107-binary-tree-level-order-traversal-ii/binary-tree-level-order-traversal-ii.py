# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#
# return its bottom-up level order traversal as:
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #自己写的，中间在各个list之间纠结了好久，结果总是把当前节点和子节点都打印出来。后来参照了solution里的答案，在给valList append的时候，append的是TreeNode的val，而不是TreeNode本身，答案就对了
        resultList = []
        currList = []
        valList = []
        if root is None: return resultList
        currList.append(root)
        while len(currList) != 0:
            nodeNumberInLevel = len(currList)
            for i in range(nodeNumberInLevel):
                t = currList.pop(0)
                valList.append(t.val)
                if t.left is not None:
                    currList.append(t.left)
                if t.right is not None:
                    currList.append(t.right)
            resultList.append(valList)
            valList = []
        resultList.reverse()
        return resultList
            
