#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    n = len(matrix)
    v_matrix = []
    i = 0

    for line in matrix:
        v_line = []
        for element in line:
            v_line.append(element)
        v_matrix.append(v_line)

    while (i < n):
        j = n - 1
        k = 0
        while (j > -1):
            matrix[i][k] = v_matrix[j][i]
            j = j - 1
            k = k + 1
        i = i + 1

