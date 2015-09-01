# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:04:29 2015

@author: SSunshine
"""

from itertools import product
from CondensedList import condensed_list


def PatternToNumber(Pattern):
    l = len(Pattern)
    
    condensed_k_mer_list = condensed_list(l)
    index = condensed_k_mer_list.index(Pattern)
    
    return index

def NumberToPattern(index, k):
    
    condensed_k_mer_list = condensed_list(k)       
    pattern = condensed_k_mer_list[index]
    
    return pattern
    
def ComputingFrequencies(text, k):

    condensed_k_mer_list = condensed_list(k)
    janky_seq_counter = {}
    
    for k_mer in condensed_k_mer_list:
        count = 0
        
        for i, bp in enumerate(text):
            end_index = i+k - 1
        
            # if you haven't gone too far down the pattern (possibility of finding k_mer still exists)        
            if end_index < len(text):
                if k_mer == text[i:i+k]: # checks that k_mer matches pattern
                    count += 1    
        janky_seq_counter[k_mer] = count
        
    return janky_seq_counter.values()