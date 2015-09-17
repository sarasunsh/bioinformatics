# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 10:12:30 2015

@author: SSunshine
"""
# breaks a sequence down into the overlapping k_mers composing it
def composition(k, text):
    k_mers = []
    text = text+text[:(k-1)]
    
    for i, bp in enumerate(text):
        end_index = i+k - 1

        # if you haven't gone too far down the pattern (possibility of finding k_mer still exists)        
        if end_index < len(text):
            k_mer = text[i:i+k]
            k_mers.append(k_mer)
            print k_mer
    
    return k_mers

#
def comp_check(k, text):
    k_mers = []
    
    for i, bp in enumerate(text):
        end_index = i+k - 1

        # if you haven't gone too far down the pattern (possibility of finding k_mer still exists)        
        if end_index < len(text):
            k_mers.append(text[i:i+k]) 
    

    if len(set(k_mers)) != len(k_mers):
        return False