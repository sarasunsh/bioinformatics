# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 14:01:19 2015

@author: SSunshine
"""

#local package imports
from HammingDistance import hamming_distance
from CondensedList import condensed_list

# finds a k-mer that has the lowest "score" (closest to consensus sequence) among a collection of strings
def median_string(strings, k):
    
    distance = float("inf") #initialize distance as zero
    possibles = condensed_list(k)
    median = "none"
  
    for p in possibles:
        if string_scores(p, strings) < distance:
            distance = string_scores(p, strings)
            median = p
    
    return median

# helper function that calculates the "score" of a k-mer (how close to consensus)
def string_scores(pattern, strings):
    k = len(pattern) # need to examine k-mers of same length as pattern
    score = 0 #initialize score as zero
    
    # go through each string to identify closest match to pattern
    for s in strings:
        
        #set hamming distance as infinity 
        ham = float("inf")
        # for each bp in sequence
        for i, bp in enumerate(s):
            end_index = i+k - 1
    
            # if you haven't gone too far down the pattern (possibilitiy of finding k_mer still exists)        
            if end_index < len(s):
                k_mer = s[i:i+k] # picks out k_mer
                if hamming_distance(k_mer, pattern) < ham:
                    ham = hamming_distance(k_mer, pattern) # set ham to lowest hamming distance (closest k-mer)
        
        score += ham
        
    return score
