# -*- coding: utf-8 -*-
"""
Created on Mon May 28 19:48:35 2018

@author: cdpengchen1
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        i = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:i+1],tin[0:i])
        root.right = self.reConstructBinaryTree(pre[i+1:],tin[i+1:])
        return root

pre = [1, 2, 3, 5, 6, 4]
tin = [5, 3, 6, 2, 4, 1]
test = Solution()
newTree = test.reConstructBinaryTree(pre, tin)
