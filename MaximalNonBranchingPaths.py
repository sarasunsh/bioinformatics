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

def nonbranching(adj_dict):

    # Initialize empty list in which nobranching paths will be added
    paths = []

    # Initializes Counter that will track which the number of OUTGOING edges
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
            
#    print "v_out, v_in"
#    print v_out, v_in

    for row in v_out.items():
        node = row[0]
        count = row[1]
#        print "node, count"
#        print node, count
#        print "v_in[node]"
#        print v_in[node]
        
        # If the node is not a 1-in-1-out node
        if count > 1 or count > v_in[node]:
#            print "entering"
#            print adj_dict[node]
            for edge in adj_dict[node]:
                path = [node, edge]
#                print "edge "+str(edge)
#                print "path"
#                print path
#                print "v_out[edge]"
#                print v_out[edge]
#                print "v_in[edge]"
#                print v_in[edge]
                
                # If added edge is a a 1-in-1-out node, continue to extend the 
                # path until you hit a node that branches
                while v_out[edge] == 1 and v_in[edge] == 1:
#                    print "adj_dict[edge] ",
#                    print adj_dict[edge]
                    path.append(adj_dict[edge][0])
                    edge = adj_dict[edge][0]
                paths.append(path)
    
    return paths
                
                
            
        
        