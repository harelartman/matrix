# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# First assignment - matrices
# Programmer - Harel Artman

import numpy as np


#smallest matrix
list1 = np.array([[1,2], [3,4]])
list2 = np.array([[5,6], [7,8], [9,10]])
FirstSmall = min(np.size(list1,0), np.size(list2,0))
SecondSmall = min(np.size(list1,1), np.size(list2,1))
m1 = np.zeros((FirstSmall,SecondSmall), int)
# m1 represnt the smallest matrix
for x in range(FirstSmall):
    for y in range(SecondSmall):
        m1[x][y] = list1[x][y] + list2[x][y]
print (m1)

#biggest matrix
FirstBig = min(np.size(list1,0), np.size(list2,0))
SecondBig = min(np.size(list1,1), np.size(list2,1))
m2 = np.zeros((FirstBig,SecondBig), int)
# m2 represnt the smallest matrix
for x in range(FirstBig):
    for y in range(SecondBig):
        if x<np.size(list1,0) and y<np.size(list1,1):
            m2[x][y] =  m2[x][y] + list1[x][y] 
        if x<np.size(list2,0) and y<np.size(list2,1):
            m2[x][y] =  m2[x][y] + list2[x][y] 
         
print (m2)
        
