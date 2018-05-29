# -*- coding: utf-8 -*-
"""
Created on Mon May 28 14:29:20 2018

@author: cdpengchen1
"""


class Solution:
    def replaceSpace(self, s):
        if len(s) == 0:
            return ''
        spaceNum = 0
        for i in s:
            if i == ' ':
                spaceNum += 1
        totalNum = len(s) + 2 * spaceNum
        newStr = totalNum * [None] 
        indexOfOriginal = len(s) - 1
        indexOfNew = totalNum - 1
        while indexOfOriginal >= 0 and indexOfNew >= indexOfOriginal:
            if s[indexOfOriginal] == ' ':
                newStr[indexOfNew - 2:indexOfNew + 1] = ['%', '2', '0']
                indexOfNew -= 3
                indexOfOriginal -= 1
            else:
                newStr[indexOfNew] = s[indexOfOriginal]
                indexOfNew -= 1
                indexOfOriginal -= 1
        return ''.join(newStr)

s = 'we are happy'
test = Solution()
a = test.replaceSpace(s)
