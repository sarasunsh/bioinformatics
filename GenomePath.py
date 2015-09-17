# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 18:38:13 2015

@author: SSunshine
"""

# Reconstruct a string from its genome path.

def genome_path(strings):
#    Input: A sequence of k-mers Pattern1, … ,Patternn such that the last k - 1 symbols of Patterni are
#                equal to the first k-1 symbols of Patterni+1 for 1 ≤ i ≤ n-1.
#     Output: A string Text of length k+n-1 such that the i-th k-mer in Text is equal to Patterni  (for 1 ≤ i ≤ n).

    genome = strings[0]
    others = strings[1:]
    
    for string in others:
        genome = genome+string[-1]
        
    return genome
    
def overlap_graph(strings):
#    Overlap Graph Problem: Construct the overlap graph of a collection of k-mers.
#    Input: A collection Patterns of k-mers.
#    Output: The overlap graph Overlap(Patterns).
    overlap = {}
    
#     for each string, select the prefix and check if it matches the suffix of other strings
#     if so, the strings with matching suffixes are adjacent
#     SOLVED: this code checks each string against itself -- this is a bug because a string could potentially return itself if it were uniform composition
    for string in strings:
        prefix = string[1:]
        adj = [string2 for string2 in strings if string2[:-1] == prefix if string2 != string]               
        if len(adj) > 0:
            overlap[string] = adj
        
    return overlap
    


                