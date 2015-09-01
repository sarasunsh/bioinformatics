# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:27:05 2015

@author: SSunshine
"""

pairs = {'A':'T', 'T':'A', 'G': 'C','C':'G'}

def reverse_DNA(Pattern):
    #  extended slice syntax. It works by doing [begin:end:step] - by leaving begin and end off and specifying a step of -1, it reverses a string.
    rev_pattern = Pattern[::-1]
    reversed_pat = ''
    
    for bp in rev_pattern:
        reversed_pat = reversed_pat + pairs[bp]
        
    return reversed_pat
    
def pattern_match(pattern, genome):
    indices = []
    k = len(pattern)
       
    for i, bp in enumerate(genome):
        end_index = i + k - 1
        # if you haven't gone too far down the pattern (possibilitiy of finding k_mer still exists)        
        if end_index < len(genome):
            if pattern == genome[i:i+k]: # checks that k_mer matches pattern
                indices.append(i)
                
    for i in indices:
        print i,