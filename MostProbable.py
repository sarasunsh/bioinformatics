# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 18:51:25 2015

@author: SSunshine
"""

# Finds the most probable k-mer in a text string (according to a profile)
def most_prob(text, k, profile):
    # text is string, k is number, profile is np.array
    
    nuc_row = {'A': 0, 'C': 1, 'G': 2, 'T':3}
    prob_tracker = {}
    most_prob = []
    
    # for each bp in first string
    for i, nuc in enumerate(text):
        end_index = i+k - 1

        # if you haven't gone too far down the pattern (possibility of finding k_mer still exists)        
        if end_index < len(text):
            k_mer = text[i:i+k] # picks out k_mer
            
            if k_mer not in prob_tracker: #don't duplicate effort
                k_mer_prob = 1   
                for i2, nuc2 in enumerate(k_mer): # select the appropriate probability for each basepair in the k-mer
                    # row number is bp_row[bp2] 
                    # column number is i2                 
                    k_mer_prob = k_mer_prob * profile[nuc_row[nuc2], i2] # calculate probability
                
                prob_tracker[k_mer] = k_mer_prob
  
    # sorts by frequency
    sorted_probs = sorted(
        prob_tracker.iteritems(),
        key=lambda x: x[1],
        reverse=True
    )

    # filters for k_mers with max probability
    filter_value = sorted_probs[0][1]
    filtered_probs = filter(
        lambda x: x[1] == filter_value,
        sorted_probs
    )
    
    # takes filtered sequences and puts them in a list
    for item in filtered_probs:
        most_prob.append(item[0])

    return most_prob   