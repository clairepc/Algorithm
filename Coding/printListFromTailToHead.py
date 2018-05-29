# -*- coding: utf-8 -*-
"""
Created on Mon May 28 15:08:30 2018

@author: cdpengchen1
"""
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self, listNode):
        if listNode.val == None:
            return
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l



node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

singleNode = ListNode(12)

test = ListNode()

S = Solution()
a = S.printListFromTailToHead(node1)
b = S.printListFromTailToHead(test)
c = S.printListFromTailToHead(singleNode)
