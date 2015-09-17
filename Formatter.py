# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 22:12:20 2015

@author: SSunshine
@ quick and dirty script
"""

#import string
#apostrophe = string.punctuation[6]
#comma = string.punctuation[11]
#colon = string.punctuation[15]
#string_break = apostrophe+comma+apostrophe

#cd C:\Users\User\Downloads
cd C:\Users\ssunshine\Downloads

with open("dataset_198_9 (3).txt") as f:
    lines = f.readlines()

content = [x.strip('\n') for x in lines]

answer = overlap_graph(content)

text_file = open("answer.txt", "w")
text_file.write(str(answer.items()))
text_file.close()




#
#dataset_file = open("dataset_198_3 (2).txt")
#strings = dataset_file.read()
##    strings = strings.strip('\n')
#    
#b = strings.split("\n")
#    
##    a = repr(strings).replace("\n", string_break)    
#
#    cd C:\Users\User\Downloads  
#    text_file = open("answer.txt", "w")
#    text_file.write(str(b))
#    text_file.close()
 
#hood= neighbors('TATTTGTCGTA',3)
#a = repr(hood).replace(",", "")
#b = a.replace("\'","")
#print b.replace(" ", "\n")
 

    

#    last_cut = 0
#    for i, l in enumerate(cookie_string):
#        if l == '=':
#            print apostrophe+cookie_string[last_cut:i]+apostrophe+colon,
#            last_cut = i+1
#        elif l == ';':
#            if i < len(cookie_string)-1:
#                print apostrophe+cookie_string[last_cut:i]+apostrophe+comma
#                last_cut= i+2
#            else: 
#                print apostrophe+cookie_string[last_cut:i]+apostrophe