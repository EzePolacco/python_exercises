#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mean_var_std.py
"""

import numpy as np

numbers_list = [0, 1, 2, 3, 4, 5,  6, 7, 8]



def calculate(numbers_list):
    
    if len(numbers_list) != 9:
        return "List must contain nine numbers."
    
    matrix = np.array(numbers_list).reshape(3, 3)
    print(matrix)

    mean = list(np.mean(matrix, axis = 0)), list(np.mean(matrix, axis = 1)), np.mean(matrix)
    mean = list(mean)

    variance = list(np.var(matrix, axis = 0)), list(np.var(matrix, axis = 1)), np.var(matrix)
    variance = list(variance)

    std = list(np.std(matrix, axis = 0)), list(np.std(matrix, axis = 1)), np.std(matrix)
    std = list(std)

    max_n = list(np.max(matrix, axis = 0)), list(np.max(matrix, axis = 1)), np.max(matrix)
    max_n = list(max_n)

    min_n = list(np.min(matrix, axis = 0)), list(np.min(matrix, axis = 1)), np.min(matrix)
    min_n = list(min_n)

    sum_n = list(np.sum(matrix, axis = 0)), list(np.sum(matrix, axis = 1)), np.sum(matrix)
    sum_n = list(sum_n)



    calculations = {
                 "mean" : list(mean),
                 "variance" : list(variance),
                 "standard deviation" : list(std),
                 "max" : list(max_n),
                 "min" : list(min_n),
                 "sum" : list(sum_n)
                 }


    return calculations

