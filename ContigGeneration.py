# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 16:08:35 2015

@author: SSunshine
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 15:50:01 2015

@author: SSunshine
"""

# This program generates all non-branching paths in a graph. It iterates 
# through all nodes of the graph that are not 1-in-1-out nodes and generates 
# all non-branching paths starting at each such node. In a final step, 
# the program finds all isolated cycles in the graph.

from collections import Counter
from GenomePath import debruijn2
from copy import deepcopy

def contig(kmers):
    
#    k = len(kmers[0])
    adj_dict = debruijn2(kmers)
    remain_d = deepcopy(adj_dict)
    
    # Initialize empty lists in which nobranching paths and isolated cycles 
    # will be added
    paths = []
    cycles = []

    # Initializes Counter that will track  the number of OUTGOING edges
    # for each node and another Counter to track INCOMING edges
    v_out = Counter()       
    v_in = Counter()   
    
    # For each node, increment the OUT counter for each connecting node while 
    # also incrementing the IN counter for those connected nodes 
    for row in adj_dict.items():
        dir_out = row[0]
        dir_ins = row[1]                     
        for ins in dir_ins:
            v_in[ins] += 1
            v_out[dir_out] += 1
    
    # Now that we have the counts to determine if a node is one-in-one-out, 
    # we will iterate through the nodes to find nonbranching paths and remove
    # them once they've been utilized
    for row in v_out.items():
        node = row[0]
        count = row[1]

        # If the node is NOT a 1-in-1-out node, it can serve as starting point
        # because it marks a branch
        if count > 1 or count != v_in[node]:          
            for i, edge in enumerate(adj_dict[node]):
                path = node + edge[-1]
                remain = adj_dict[node][i:]
                remain_d[node] = remain
                
                # If added edge is a a 1-in-1-out node, continue to extend the 
                # path until you hit a node that branches
                while v_out[edge] == 1 and v_in[edge] == 1:
                    path = path + adj_dict[edge][0][-1]
                    
                    # BUG: modifying edge inside a program which iterates 
                    # through edge is not good practice - alternative approach?
                    edge = adj_dict[edge][0]
                    
                # Add path to collection of nonbranching paths
                paths.append(path)
                
                
        # Find isolated cycles in the graph
        # ---QUESTION: if a cycle is isolated (disconnected from the rest of the graph) 
        # ---but has a branch in it, should it be added as a nonbranching path?
        # ---Under this code, it is not.
        
        # If the node is 1-in-1-out, it may be the start of an isolated cycle
        elif count == 1 and v_in[node] == 1:
            start = node
            edge = adj_dict[node][0]
            cycle = start + edge[-1]
            # If added edge is a a 1-in-1-out node, continue to extend the 
            # path until you hit a node that branches (eliminating the path as 
            # a possible cycle) or the starting node (completing the cycle)
            while v_out[edge] == 1 and v_in[edge] == 1:
                cycle = cycle + adj_dict[edge][0][-1]
                edge = adj_dict[edge][0]
                if edge == start:
                    cycles.append(cycle)
                    break
                
    # Filter cycles for uniques
    uniq_cyc_nodes = []
    for cyc in cycles:
        # Check if the starting node of the cycle has already been used in a 
        # cycle. If it has not, add the cycle to path and its nodes to a tracker.
        if cyc[0] not in uniq_cyc_nodes:
            paths.append(cyc)
            for i, n in enumerate(cyc):
                uniq_cyc_nodes.append(n)
            
            
    return paths