# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 19:28:58 2015

@author: SSunshine
"""
# Local Package Imports
from FrequentWordsWithMismatch import neighbors
from PatternCount import approx_pattern_count
   

def motif_enum(strings, k, d):
    patterns = []        
    
    # first string in the strings will be analyzed first
    first_string = strings[0]
    other_string_range = range(1, len(strings))
    
    # go through each bp in first string
    for i, bp in enumerate(first_string):
        end_index = i+k - 1

        # if you haven't gone too far down the pattern (possibility of finding k_mer still exists)        
        if end_index < len(first_string):
            k_mer = first_string[i:i+k] # picks out k_mer          
            hood = neighbors(k_mer, d) # generates neighbors of k_mer
            
            for p in hood:
                # for each neighbor of the k-mer, go through the other strings to see if closely related k-mers are there                       
                for j in other_string_range: # iterates through the rest of the strings             
                    if approx_pattern_count(p, strings[j], d) ==0: # checks if there are any related k-mers
                        break # if the next string doesn't have a neighbor of the neighbor, skip it
                else:
                    patterns.append(p) # if the neighbor has a neighbor in each string (has made it past the 'break' in each string), it gets added
    
    patterns = list(set(patterns))
    
    return patterns
  