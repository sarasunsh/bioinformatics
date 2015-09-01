# -*- coding: utf-8 -*-
"""
Created on Fri May 22 13:59:54 2015

@author: SSunshine
"""

def hamming_distance(p,q):
    hams = 0    
    for i, bp in enumerate(p):
        if bp != q[i]:
            hams += 1
    
    return hams
