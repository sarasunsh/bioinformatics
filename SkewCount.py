# -*- coding: utf-8 -*-
"""
Created on Fri May 22 09:10:20 2015

@author: SSunshine
"""

def skew(genome):
    skew_map = {}    # create dict of i to skew values
    skew = 0
    
    #calculate initial skew based on first position
    for bp in genome:
            if bp == 'C':
                skew -= 1
            elif bp == 'G':
                skew += 1
    skew_map[0] = skew
    
    # The skew for each position after the first is
    # only one different from the previous position's skew.
    # So you can just go through each position and figure how it's different  
    i = 1                    
    while i < len(genome):
        if genome[i-1] == 'C':
            skew += 1
        elif genome[i-1] == 'G':
            skew -= 1
        skew_map[i] = skew
        i += 1
    
    # sorts skew(i) by minimization
    sorted_skews = sorted(
        skew_map.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # filters for skews that achieve minimization
    filter_value = sorted_skews[0][1]
    filtered_skews = filter(
        lambda x: x[1] == filter_value,
        sorted_skews
    )
    
    return filtered_skews
        