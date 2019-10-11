# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:17:56 2019

@author: miles
"""
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

ij = input('Enter X,Y (X = no. of rows, Y = no. of columns): ').split(',')  
ij = [int(ij[ind]) for ind in [0,1]] #[X,Y]

array = [[0 for yval in list(range(ij[1]))] for xval in list(range(ij[0]))] #error here was having each of the rows pointing to the same 'zerorow' variable, so changing one row changed them all

for row_ind in [i for i in range(ij[0])]:
    for col_ind in [i for i in range(ij[1])]:
        array[row_ind][col_ind] = row_ind*col_ind

print(array)
    
    
    
    
    
    