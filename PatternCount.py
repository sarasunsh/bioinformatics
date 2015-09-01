# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:54:01 2015

@author: SSunshine
"""

def pattern_count(text, pattern):
    count = 0
    for i, b in enumerate(text):
        # if index is far enough from end of sequence that possibility of finding pattern still exists
        if i < (1+ len(text) - len(pattern)): 
            # if the section of text matches the pattern
            if text[i: i+len(pattern)] == pattern:
                count += 1
    return count

# Local Package Imports
from HammingDistance import hamming_distance
   
def approx_pattern_count(pattern, text, d):
    positions = []
    for i, b in enumerate(text):
        # if index is far enough from end of sequence that possibility of finding pattern still exists
        if i < (1+ len(text) - len(pattern)): 
            # if the section of text matches the pattern
            if text[i: i+len(pattern)] == pattern:
                positions.append(i) # add it to the list of positions
            elif hamming_distance(pattern, text[i: i+len(pattern)]) <= d:
                 positions.append(i)
    print positions    
    print len(positions)
    
    return len(positions)



