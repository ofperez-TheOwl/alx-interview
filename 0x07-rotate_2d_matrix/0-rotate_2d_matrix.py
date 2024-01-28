#!/usr/bin/python3
"""
rotate 2D Matrix
It rotates a suare matrix by 90 degre clockwise
TheOwl
"""
def rotate_2d_matrix(matrix):
    n = len(matrix)

    #rotattion can be assimilate to the composition of a transposition and reversion
    
    #transposition
    for i in range(n):
        for j in range (i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # reversion
    for i in range(n):
        matrix[i].reverse()
