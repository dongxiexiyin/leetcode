# Invert a binary tree.
#
# Example:
#
# Input:
#
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
# Output:
#
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
#
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
#
# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #自己没想出来，想得有点复杂，其实很简单，从每个子树的叶子节点开始左右交换，然后返回父节点，依次进行直至根节点。注意，每次交换的是节点而非节点的值
        #递归
        '''
        if root is None: return None
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root
        '''
        #循环，需要借助一个list或者deque保存树中的节点，先把每个节点的左右孩子交换，然后把左右孩子入队，None值不入队
        #二叉树的好多算法用循环写的时候都需要借助一个队列保存节点，这点要注意
        if root is None: return None
        resultList = []
        resultList.append(root)
        while len(resultList) != 0:
            curr = resultList.pop()
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            if curr.left is not None: resultList.append(curr.left)
            if curr.right is not None: resultList.append(curr.right)
        return root
