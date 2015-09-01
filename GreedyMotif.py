# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 19:45:52 2015

@author: SSunshine
"""
import numpy as np
import random
from collections import Counter


def greedy(strings, k, t):
    """
    Function greedy: meow meow, the bees knees
    
    @param strings: meow IT"S A STRING that does this
    @param k: int, meow 
    @param t: int, meow
    @return
    """
    # strings is a list, k and t are integers
    
    #set the best_motifs as the first k_mers in each string, just as a starting point
    best_motifs = [string[:k] for string in strings]
    best_prof, best_score = calc_score(best_motifs)
    
    rang = range(len(strings)) 
    #creates list of indexes starting at 1
    rang.pop(0)
    
    # for each k-mer in the first string
    for i, bp in enumerate(strings[0]):
        end_index = i+k - 1
        motifs = []
        # if you haven't gone too far down the pattern (possibility of finding k_mer still exists)        
        if end_index < len(strings[0]):
            motifs.append(strings[0][i:i+k]) # picks out k-mer for starting point

#            print "i: "+str(i)
#            print "k-mer (motif1): "+strings[0][i:i+k]

            # for each of the remaining strings
            for r in rang:
                
                profile, score = calc_score(motifs) # calculate the profile of motifs selected so far
                motif_r = most_prob(strings[r], k, profile) # find the most probable motif in the next string
#                print "r: "+str(r)                
#                print "profile: "
#                print profile                
#                print "strings[r]: "+strings[r]
#                print "motif_r (full list): ",
#                print motif_r

#                if len(motif_r) > 1: # if there are multiple "most probable" motif, pick one at random
#                    motif_r = random.choice(motif_r)
#                else:
#                    motif_r = motif_r[0] # converts from list (as returned by most_prob) to string
                motif_r = motif_r[0] # converts from list (as returned by most_prob) to string
                motifs.append(motif_r)
#                print "motifs after appending: ",
#                print motifs
                
            profile, score = calc_score(motifs) # calculate score once again after each string has been reviewed
#            print "score once appended: "+str(score)
            
            if score < best_score:
                best_score = score
                best_motifs = motifs
#                print "better score"
#    
    return best_motifs
            
    
# helper function to generate probability profile and score based on a set of strings
def calc_score(strings):
    # define constants
    string_length = len(strings[0])
    profile = np.zeros((4, string_length)) # create empty profile array
    nuc_row = {'A': 0, 'C': 1, 'G': 2, 'T':3}
    score = 0

    nuc_counter = Counter()
    highest_prob = 0    
    col_range = range(string_length)   
    for i in col_range: # for each position in the string
        for s in strings: # go through each string
            nuc_counter[s[i]] += 1 # count appearances of a nucleotide in i position of a string
#            print "s[i]: "+s[i]
#        print "nuc_counter.items(): ",nuc_counter.items()
        for row in nuc_counter.items():
            prob = float(row[1]) / len(strings) # calculate probability 
            profile[nuc_row[row[0]], i] = prob # set profile accordingly
#            print "prob: "+str(prob)
#            print "profile: "
#            print profile

            if prob > highest_prob:
                highest_prob = prob # picks out most likely nucleotide in each column
#                print "prob > highest_prob"

        score += (1.0 - highest_prob)*10  # converts probability to score
        highest_prob = 0
        nuc_counter = Counter() # reset counter to calculate next column
        i += 1 # move on to next column
#        print "score: "+str(score)
        
    return (profile, score)
    
# Finds the most probable k-mer in a text string (according to a profile)
def most_prob(text, k, profile):
    # text is string, k is number, profile is np.array
    
    nuc_row = {'A': 0, 'C': 1, 'G': 2, 'T':3}
    prob_tracker = {}
    most_prob = []
    
    # for each bp in text
    for i, nuc in enumerate(text):
        end_index = i+k - 1

        # if you haven't gone too far down the pattern (possibility of finding k_mer still exists)        
        if end_index < len(text):
            k_mer = text[i:i+k] # picks out k_mer
#            print "k_mer: "+k_mer
            
            if k_mer not in prob_tracker: #don't duplicate effort
                k_mer_score = 0   
                for i2, nuc2 in enumerate(k_mer): # select the appropriate probability for each basepair in the k-mer
                    # row number is bp_row[bp2] 
                    # column number is i2  
#                    print "i2: "+str(i2)
#                    print "nuc2: "+str(nuc2)
#                    print "profile[nuc_row[nuc2]: "+str(profile[nuc_row[nuc2], i2])
                    # if the nucleotide's probability in that position is zero
                    k_mer_score += (1.0 - profile[nuc_row[nuc2], i2])*10 # converts probability to score
#                    print "k_mer_score: "+str(k_mer_score)
                prob_tracker[k_mer] = k_mer_score
#                print prob_tracker
  
    # sorts by frequency
    sorted_probs = sorted(
        prob_tracker.iteritems(),
        key=lambda x: x[1],
        reverse=False
    )

    # filters for k_mers with max probability
    filter_value = sorted_probs[0][1]
    filtered_probs = filter(
        lambda x: x[1] == filter_value,
        sorted_probs
    )
    
    # takes filtered sequences and puts them in a list
    for item in filtered_probs:
        most_prob.append(item[0])

    return most_prob   