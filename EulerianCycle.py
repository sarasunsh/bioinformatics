# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 11:04:41 2015

@author: SSunshine
"""

# local package import
import random
from copy import deepcopy
from collections import Counter

# Solve the Eulerian Path Problem.
#     Input: The adjacency list of an Eulerian directed path.
#     Output: An Eulerian path in this graph.

# IMPORTANT: this program assumes that it is possible to create a Eulerian 
# path from the input

def eulerian_path(adj_dict):
    
    # Adjacency dictionary with 'false' edge added to make a cycle
    cycle_d = deepcopy(adj_dict)

    # Initializes Counter that will track which nodes are unbalanced, 
    # which gives us the start and finish
    find_ends = Counter()    
    
    # Go through each node, using the counter find_ends to count how many nodes 
    # are adjacent to the current node and subtract 1 for each of those adj
    for row in cycle_d.items():
        dir_out = row[0]
        dir_ins = row[1]        
                
        for ins in dir_ins:
            find_ends[ins] -= 1
            find_ends[dir_out] += 1

    # The most_common function return a list of elements and their counts 
    # from the most common to the least.
    # The starting node (V0) will be most common, as there is 1 less node 
    # adjacent to it, while the ending node will have 1 less adjacency
    start = find_ends.most_common()[0][0]
    end = find_ends.most_common()[-1][0]
    
    # Create a 'false' edge between the end node and the start node so as to
    # enable the algorithm for Eulerian cycles to function
    try:
        cycle_d[end].append(start)
    except KeyError:
        cycle_d[end] = [start]
        
    cycle = eulerian_cycle(cycle_d)
    
    # Eulerian cycle needs to be re-oriented to begin with the "true" starteulerian_
    for i, n in enumerate(cycle):
        if n == end:
            if cycle[i+1] == start:
                break_point = i
                break
    
    cycle =  cycle[break_point+1:] + cycle[1:break_point+1]   
    
    return cycle  

def eulerian_cycle(adj_dict):
    
    # Dictionary that tracks remaining edges (those not yet taken),
    # initialized as the input adjacency dict
    remain_d = deepcopy(adj_dict)
    
    # Randomly select a starting node
    node = random.choice(range(len(adj_dict)))
    
    # Create list to track Eulerian cycle
    cycle= [node] 

    # Continue as long as there are edges that remain untaken    
    while len(remain_d) > 0:

        # Check if any adjacencies remain for the node and if so, how many        
        value = remain_d.get(node)
        
        # If the node has no unused edges, we must be back at V0 (since the 
        # graph is balanced), but we also know there are remaining edges out 
        # there. We need to expand the circle until it encompasses all nodes.
        if value == None:
                       
            # To do so, iterate through the current "cycle" until we find a 
            # node with an unused edge. Make that the new V0.
            for i, n in enumerate(cycle):
                if remain_d.get(n) > 0:
                    node = n
                    cycle = cycle[i:]+cycle[1:i+1]
                    break
                
        # If the node has a single unused edge, simply use it to continue the 
        # cycle by adding it to the list 'cycle' and removing it from the dict
        elif len(value) == 1:       
            node = remain_d.pop(node)[0]
            cycle.append(node)
            
        # If the node has multiple unused edges, randomly select one to add to 
        # the cycle and remove it out from the node's list of adjacencies.
        elif len(value) > 1:
            random_i = random.randrange(len(value))
            pos_nodes = remain_d[node]
            new_node = pos_nodes.pop(random_i) 
            remain_d[node] = pos_nodes
            node = new_node
            cycle.append(node)

    return cycle