# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 19:02:46 2015

@author: SSunshine
"""

#You now have a method to assemble a genome, since the String Reconstruction Problem reduces to finding an Eulerian path in the de Bruijn graph generated from reads.
#
#CODE CHALLENGE: Solve the String Reconstruction Problem.
#     Input: An integer k followed by a list of k-mers Patterns.
#     Output: A string Text with k-mer composition equal to Patterns. (If multiple answers exist, you may
#     return any one.)

#IMPORTANT: this program assumes that it is possible to create a path from the input and that each node has only one overlapping node

# local package import
import random
from copy import deepcopy
from collections import Counter
from GenomePath import debruijn2

def reconstruction(kmers):
    
    # Use De Bruijn approach to create adjacency dictionary from list of k-mers
    adj_dict = debruijn2(kmers)    

    # Create dictionary that tracks remaining edges (those not yet taken)
    remain_d = deepcopy(adj_dict)

    # Initializes Counter that will track which nodes are unbalanced, 
    # which gives us the start and finish    
    find_ends = Counter()

    # Go through each node, using the counter find_ends to count how many nodes 
    # are adjacent to the current node and subtract 1 for each of those adj       
    for row in remain_d.items():
        dir_out = row[0]
        dir_ins = row[1]        
                
        for ins in dir_ins:
            find_ends[ins] -= 1
            find_ends[dir_out] += 1
            
    # The most_common function return a list of elements and their counts 
    # from the most common to the least.
    # The starting node will be most common, as there is 1 less node 
    # adjacent to it, while the ending node will have 1 less adjacency
    node = find_ends.most_common()[0][0]
           
    # Begin to reconstruct the string
    reconstructed = node
    
    # Continue as long as there are edges remaining untaken    
    while len(remain_d) > 0:
        node = remain_d.pop(node)[0]
        reconstructed = reconstructed+node[-1]
        
    return reconstructed  

