# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 11:04:41 2015

@author: SSunshine
"""

# local package import
import random
from copy import deepcopy

#Solve the Eulerian Cycle Problem.
#     Input: The adjacency list of an Eulerian directed graph.
#     Output: An Eulerian cycle in this graph.

#IMPORTANT: this program assumes that it is possible to create a Eulerian cycle from the input

def eulerian(adj_dict):
    
    # dictionary that tracks remaining edges (those not yet taken)
    remain_d = deepcopy(adj_dict)
    
    # randomly picks a starting node
#    node = random.choice(range(len(adj_dict)))
    node = adj_dict.items()[0][0] # start with the first node listed
    cycle= [node] # list that tracks the Eulerian cycle

    # continue as long as there are edges remaining untaken    
    while len(remain_d) > 0:
#        print "BACK AT THE TOP"
#        print "node: "+str(node)
        value = remain_d.get(node)
#        print "remain_d"
#        print remain_d
#        print "length: "+str(len(remain_d))
#        print "node: "+str(node)
#        print "value: "+str(value)
#        print "cycle: "
#        print cycle
        if value == None:
            # if the node has no unused edges, it must be back at the original point (since graph is balanced)
            # so we want to expand the circle until it encompasses all nodes
#            print "ENTERING THIRD CONDITION"            
            for i, n in enumerate(cycle):
#                print "n: "+str(n)
#                print "i: "+str(i)
                if remain_d.get(n) > 0:
                    node = n
                    cycle = cycle[i:]+cycle[1:i+1]
                    break
#            print "remain_d"
#            print remain_d
#            print len(remain_d)
#            print "node: "+str(node)
#            print "cycle: "
#            print cycle

        elif len(value) == 1: # if the starting point only links to one other node, no choices to be made here
#            print "ENTERING FIRST CONDITION"            
            node = remain_d.pop(node)[0]
            cycle.append(node)
#            print "remain_d"
#            print remain_d
#            print len(remain_d)
#            print "node: "+str(node)
#            print "cycle: "
#            print cycle
        elif len(value) > 1:
            # randomly picks one of the edges to follow and removes it from remain_d
#            print "ENTERING SECOND CONDITION"            
            random_i = random.randrange(len(value))
#            print "random_i: "+str(random_i)
            pos_nodes = remain_d[node]
#            print "pos_nodes: ",
#            print pos_nodes
            new_node = pos_nodes.pop(random_i)
#            print "new_node: "+str(new_node)
            remain_d[node] = pos_nodes
            node = new_node
            cycle.append(node)
#            print "remain_d"
#            print remain_d
#            print len(remain_d)
#            print "node: "+str(node)
#            print "cycle: "
#            print cycle
        elif value == None:
            # if the node has no unused edges, it must be back at the original point (since graph is balanced)
            # so we want to expand the circle until it encompasses all nodes
#            print "ENTERING THIRD CONDITION"            
            for i, n in enumerate(cycle):
#                print "n: "+str(n)
#                print "i: "+str(i)
                if remain_d.get(n) > 0:
                    node = n
                    cycle = cycle[i:]+cycle[:i+1]
                    break
#            print "remain_d"
#            print remain_d
#            print len(remain_d)
#            print "node: "+str(node)
#            print "cycle: "
#            print cycle
#            
    return cycle  