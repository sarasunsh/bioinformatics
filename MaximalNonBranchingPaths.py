# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 15:50:01 2015

@author: SSunshine
"""

#MaximalNonBranchingPaths(Graph)
#        Paths ← empty list
#        for each node v in Graph
#            if v is not a 1-in-1-out node
#                if out(v) > 0
#                    for each outgoing edge (v, w) from v
#                        NonBranchingPath ← the path consisting of the single edge (v, w)
#                        while w is a 1-in-1-out node
#                            extend NonBranchingPath by the outgoing edge (w, u) from w 
#                            w ← u
#                        add NonBranchingPath to the set Paths
#        for each isolated cycle Cycle in Graph
#            add Cycle to Paths
#        return Paths

from copy import deepcopy
from collections import Counter

def nonbranching(adj_dict):

    # Initializes Counter that will track which nodes are unbalanced, 
    # which gives us the start and finish
    v_out = Counter()       
    v_in = Counter()   
    
    # Go through each node, using the counter find_ends to count how many nodes 
    # are adjacent to the current node and subtract 1 for each of those adj
    for row in adj_dict.items():
        dir_out = row[0]
        dir_ins = row[1]        
                
        for ins in dir_ins:
            v_out[ins] += 1
            v_in[dir_out] += 1

    return v_out, v_in