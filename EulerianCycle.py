# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 11:04:41 2015

@author: SSunshine
"""

# local package import
import random

#Solve the Eulerian Cycle Problem.
#     Input: The adjacency list of an Eulerian directed graph.
#     Output: An Eulerian cycle in this graph.

#IMPORTANT: this program assumes that it is possible to create a Eulerian cycle from the input

def eulerian(adj_dict):
    
    # dictionary that tracks remaining edges (those not yet taken)
    remain_d = adj_dict
    
    # randomly picks a starting node
    node = random.choice(range(len(adj_dict)))
    cycle= [node] # list that tracks the Eulerian cycle

    # continue as long as there are edges remaining untaken    
    while len(remain_d) > 0:
        value = remain_d.get(node)
        if len(value) == 1: # if the starting point only links to one other node, no choices to be made here
            node = remain_d.pop(node)[0]
            cycle.append[node]
        elif len(value) > 1:
            # randomly picks one of the edges to follow and removes it from remain_d
            random_i = random.randrange(len(value))
            node = remain_d[value].pop(random_i)
            cycle.append[node]
        elif value == None:
            
            
            
            
#    for row in adj_dict.items():
#        if len(row[1]) >1:
#    
    