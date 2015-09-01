# -*- coding: utf-8 -*-
"""
This function generates a list of 

Created on Tue Jul 21 20:46:05 2015

@author: SSunshine
"""
# Local Package Imports
from HammingDistance import hamming_distance
from ReverseCompliment import reverse_DNA
from collections import Counter

#generate the d-neighborhood of a k-mer pattern.
def neighbors(pattern, d):
       
    bases = ['A', 'C', 'G', 'T']  # basepair library
    
    if d == 0: # if no differences allowed, no need to generate neighbors
        return pattern
    if len(pattern) == 1: #if pattern is one basepair, other basepairs only possible neighbors
        return bases
    
    first = pattern[0]    # start by popping off first letter of pattern
    neighborhood = []
    suf_neighbors = neighbors(pattern[1:], d) #recursively generate smaller and smaller slices
        
    
    for t in suf_neighbors: 
        if hamming_distance(pattern[1:], t) < d:
            for b in bases:
                neighborhood.append(b+t)
        else:
            neighborhood.append(first+t)
    return neighborhood



def freq_word_mismatch(text, k, d):
    freq_patterns = [] # no frequent patterns found yet
    seq_counter = Counter() # create a counter
    seq_dict = {}

    # for each bp in sequence
    for i, bp in enumerate(text):
        end_index = i+k - 1

        # if you haven't gone too far down the pattern (possibilitiy of finding k_mer still exists)        
        if end_index < len(text):
            k_mer = text[i:i+k] # picks out k_mer
            hood = neighbors(k_mer, d) # generates neighbors of k_mer

            for p in hood:                
                seq_counter[p] += 1 # count as an occurrence of each neighbor

#    
    # calculate the sum Countd(Text, Pattern)+ Countd(Text, ReversePattern)
    for row in seq_counter.items():
        seq_dict[row[0]] = row[1] + seq_counter[reverse_DNA(row[0])]
    
    # sorts k_mers by frequency
    sorted_sequences = sorted(
        seq_dict.iteritems(),
        key=lambda x: x[1],
        reverse=True
    )

    # filters for k_mers with max frequency
    filter_value = sorted_sequences[0][1]
    filtered_sequences = filter(
        lambda x: x[1] == filter_value,
        sorted_sequences
    )
    
    # takes filtered sequences and puts them in a list
    for item in filtered_sequences:
        freq_patterns.append(item[0])

    return freq_patterns    