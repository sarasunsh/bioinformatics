# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:05:56 2015

@author: SSunshine
"""
from itertools import product

def condensed_list(k):
    #generates alphabetically ordered list of all possible sequences of length k    
    
    k_mer_list = []
    bp = ['A', 'T', 'C', 'G']
   
    # generates list of tuples with every possible k_mer
    for k_mer in product(bp, repeat = k):
        k_mer_list.append(k_mer)

    # sorts k_mers in alphabetical order (is this necessary?)
    k_mer_list = sorted(k_mer_list)
    
    # since k_mer_list is in tuple format and we want it to be condensed string, we have to convert
    condensed_k_mer_list = []
    for row in k_mer_list:
        l = len(row)
        if l < 2:
            condensed_k_mer_list.append(row)
        else:
            condensed = ''
            for item in row:
                condensed = condensed+item
            condensed_k_mer_list.append(condensed)
    
    return condensed_k_mer_list
    
def condensed_list_b(k):
    #generates alphabetically ordered list of all possible sequences of length k    
    
    k_mer_list = []
    bp = ['0', '1']
   
    # generates list of tuples with every possible k_mer
    for k_mer in product(bp, repeat = k):
        k_mer_list.append(k_mer)

    # sorts k_mers in alphabetical order (is this necessary?)
    k_mer_list = sorted(k_mer_list)
    
    # since k_mer_list is in tuple format and we want it to be condensed string, we have to convert
    condensed_k_mer_list = []
    for row in k_mer_list:
        l = len(row)
        if l < 2:
            condensed_k_mer_list.append(row)
        else:
            condensed = ''
            for item in row:
                condensed = condensed+item
            condensed_k_mer_list.append(condensed)
    
    return condensed_k_mer_list
