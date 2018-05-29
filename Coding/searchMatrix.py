# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:46:41 2018

@author: cdpengchen1
"""

array = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]
array2 = []
array3 = [['a', 'b', 'c'],
          ['b', 'c', 'd']]
array4 = [[62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80],[63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81],[64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82],[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83],[66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84],[67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85]]

class Solution:
    # array 二维列表
    def Find(self, array, target):
        if len(array) == 0 :
            return False
        ncol = len(array[0])
        nrow = len(array)
        i = 0
        j = ncol - 1

        # if type(target) == float and type(array[0][0]) == int:
        #     target = int(target)
        # elif type(target) == int and type(array[0][0]) == float:
        #     target = float(target)
        # elif type(target) != type(array[0][0]):
        #     return False

        while i <= nrow - 1 and j >= 0:
            key = array[i][j]
            if target > key:
                i += 1
            elif target < key:
                j -= 1
            else:
                return True
        return False

    def searchMatrix(self, matrix, target):
        if len(array) == 0 :
            return 0
        ncol = len(array[0])
        nrow = len(array)
        i = 0
        j = ncol - 1
        count = 0
        while i <= ncol - 1 and j >= 0:
            key = array[i][j]
            if target > key:
                i += 1
            elif target < key:
                j -= 1
            else:
                count += 1
                j -= 1
        return count

findtarget = Solution()
a = findtarget.searchMatrix(array, 9)
