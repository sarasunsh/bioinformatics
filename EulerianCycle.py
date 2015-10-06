# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 11:04:41 2015

@author: SSunshine
"""

# local package import
import random
from copy import deepcopy
from collections import Counter

#Solve the Eulerian Path Problem.
#     Input: The adjacency list of an Eulerian directed path.
#     Output: An Eulerian path in this graph.

#IMPORTANT: this program assumes that it is possible to create a Eulerian path from the input

def eulerian(adj_dict):
    # dictionary that tracks remaining edges (those not yet taken)
    remain_d = deepcopy(adj_dict)

    find_ends = Counter()    
    
    for row in remain_d.items():
        dir_out = row[0]
        dir_ins = row[1]        
                
        for ins in dir_ins:
            find_ends[ins] -= 1
            find_ends[dir_out] += 1

    start = find_ends.most_common()[0][0]
    end = find_ends.most_common()[-1][0]
    
    try:
        remain_d[end].append(start)
    except KeyError:
        remain_d[end] = [start]

   
    # randomly picks a starting node
    node = random.choice(range(len(adj_dict)))
#    node = adj_dict.items()[0][0] # start with the first node listed
    cycle= [node] # list that tracks the Eulerian cycle

    # continue as long as there are edges remaining untaken    
    while len(remain_d) > 0:

        value = remain_d.get(node)
        if value == None:
            # if the node has no unused edges, it must be back at the original point (since graph is balanced)
            # so we want to expand the circle until it encompasses all nodes          
            for i, n in enumerate(cycle):
                if remain_d.get(n) > 0:
                    node = n
                    cycle = cycle[i:]+cycle[1:i+1]
                    break
        elif len(value) == 1: # if the starting point only links to one other node, no choices to be made here        
            node = remain_d.pop(node)[0]
            cycle.append(node)
        elif len(value) > 1:
            # randomly picks one of the edges to follow and removes it from remain_d     
            random_i = random.randrange(len(value))
            pos_nodes = remain_d[node]
            new_node = pos_nodes.pop(random_i)
            remain_d[node] = pos_nodes
            node = new_node
            cycle.append(node)

        elif value == None:
            # if the node has no unused edges, it must be back at the original point (since graph is balanced)
            # so we want to expand the circle until it encompasses all nodes           
            for i, n in enumerate(cycle):
                if remain_d.get(n) > 0:
                    node = n
                    cycle = cycle[i:]+cycle[:i+1]
                    break


    for i, n in enumerate(cycle):
        if n == end:
            if cycle[i+1] == start:
                break_point = i
                break
    
    cycle =  cycle[break_point+1:] + cycle[1:break_point+1]   
    
    return cycle  