# -*- coding: utf-8 -*-
"""
Created on Mon Sep 07 23:05:27 2015

@author: User
"""

#     Input: Integers k and t, followed by a collection of strings Dna.
#     Output: A collection BestMotifs resulting from running RANDOMIZEDMOTIFSEARCH(Dna, k, t) 
#     1,0000 times. Remember to use pseudocounts!
#
#
#Sample Input:
#     8 5
#     CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
#     GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
#     TAGTACCGAGACCGAAAGAAGTATACAGGCGT
#     TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
#     AATCCACCAGCTCCACGTGCAATGTTGGCCTA
#
#Sample Output:
#     TCTCGGGG
#     CCAAGGTG
#     TACAGGCG
#     TTCAGGTG
#     TCCACGTG

# local package imports
import random

def randomized_motif(strings, k, t):
        """
    Function randomized_motif: search for the most likely motifs using randomly chosen k-mers as a starting point
    
    @param strings: collection of strings in list format
    @param k: int, k-merlength
    @param t: int, number of strings
    @return
    """
    
    motifs = []    
    
    # for each DNA string, generate random index and pick k-mer
    for string in strings:
        i = random.randint(0, len(strings[0])-k)                
        motifs.append(string[i:i+k])
        
# helper function to generate probability profile (with pseudocounts) based on a set of strings
def calc_profile(strings):
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
            prob = float(row[1]) / len(strings) + 1 # calculate probability 
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