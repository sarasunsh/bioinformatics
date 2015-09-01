# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:06:44 2015

@author: SSunshine
"""

from collections import Counter
    
def freq_words(text, k):
    freq_patterns = [] # no frequent patterns found yet
    seq_counter = Counter() # create a counter

    # for each bp in sequence
    for i, bp in enumerate(text):
        end_index = i+k - 1
        # if you haven't gone too far down the pattern (possibilitiy of finding k_mer still exists)        
        if end_index < len(text):
            k_mer = text[i:i+k] # picks out k_mer
            seq_counter[k_mer] += 1
   
    # sorts k_mers by frequency
    sorted_sequences = sorted(
        seq_counter.items(),
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
    

