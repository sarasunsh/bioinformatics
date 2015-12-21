# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 09:16:38 2015

@author: sara
"""

# Takes a set of read-pairs length k with gap length d and reconstructs a string
# Input: list of lists
# Output: string

def read_pairs(pairs, d):
    
    first_seq = pairs[0][0][:-1]
    k = len(first_seq)+1
    sec_seq = pairs[0][1][:-1]
    
#    print first_seq, k, sec_seq, "Now let's move"

    for row in pairs:
        first_seq = first_seq+row[0][-1]
        sec_seq = sec_seq+row[1][-1]
#        print first_seq, sec_seq
    
    adjust = k+d
    for i, bp in enumerate(first_seq):
        if i > adjust-1:        
#            print "i, bp ", i, bp
#            print i-adjust
            if bp != sec_seq[i-adjust]:
                return "there is no string spelled by the gapped patterns"
            
    # return PrefixString concatenated with the last k + d symbols of SuffixString        
    final_seq = first_seq + sec_seq[-adjust:]
    
    return final_seq