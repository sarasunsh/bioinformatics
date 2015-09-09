# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 10:12:30 2015

@author: SSunshine
"""

def composition(k, text):
    k_mers = []
    
    for i, bp in enumerate(text):
        end_index = i+k - 1

        # if you haven't gone too far down the pattern (possibility of finding k_mer still exists)        
        if end_index < len(text):
            k_mers.append(text[i:i+k]) 
    
    return set(k_mers)