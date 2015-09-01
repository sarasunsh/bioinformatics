# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:12:56 2015

@author: SSunshine
"""

def find_clumps(genome, k, l, t):
    freq_patterns = [] # no frequent patterns found yet

    # for each bp in sequence
    for i, bp in enumerate(genome):
        end_index = i+k
        if end_index < len(genome):
            k_mer = genome[i:i+k]        
            mini_genome = genome[i:i+l]        
    
            if mini_genome.count(k_mer) == t:
                freq_patterns.append(k_mer)
        
   #return freq_patterns
    unique_freq_patterns = list(set(freq_patterns))
    for item in unique_freq_patterns:
        print item,