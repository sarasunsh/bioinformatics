# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 14:06:21 2016

@author: sara
"""

codons = {'AAA': 'K',
 'AAC': 'N',
 'AAG': 'K',
 'AAU': 'N',
 'ACA': 'T',
 'ACC': 'T',
 'ACG': 'T',
 'ACU': 'T',
 'AGA': 'R',
 'AGC': 'S',
 'AGG': 'R',
 'AGU': 'S',
 'AUA': 'I',
 'AUC': 'I',
 'AUG': 'M',
 'AUU': 'I',
 'CAA': 'Q',
 'CAC': 'H',
 'CAG': 'Q',
 'CAU': 'H',
 'CCA': 'P',
 'CCC': 'P',
 'CCG': 'P',
 'CCU': 'P',
 'CGA': 'R',
 'CGC': 'R',
 'CGG': 'R',
 'CGU': 'R',
 'CUA': 'L',
 'CUC': 'L',
 'CUG': 'L',
 'CUU': 'L',
 'GAA': 'E',
 'GAC': 'D',
 'GAG': 'E',
 'GAU': 'D',
 'GCA': 'A',
 'GCC': 'A',
 'GCG': 'A',
 'GCU': 'A',
 'GGA': 'G',
 'GGC': 'G',
 'GGG': 'G',
 'GGU': 'G',
 'GUA': 'V',
 'GUC': 'V',
 'GUG': 'V',
 'GUU': 'V',
 'UAA': ' ',
 'UAC': 'Y',
 'UAG': ' ',
 'UAU': 'Y',
 'UCA': 'S',
 'UCC': 'S',
 'UCG': 'S',
 'UCU': 'S',
 'UGA': ' ',
 'UGC': 'C',
 'UGG': 'W',
 'UGU': 'C',
 'UUA': 'L',
 'UUC': 'F',
 'UUG': 'L',
 'UUU': 'F'}


def amino_translate(rna):
    protein = ''
    for i, bp in enumerate(rna):
#        print i, " i"
        if i == 0 or i%3 == 0:
#            print "past if"
            amino = codons[rna[i:i+3]]
#            print amino," amino"
#            print rna[i:i+3]
            if amino == ' ':
                return protein
            else:
                protein = protein+amino