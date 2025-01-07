# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 19:29:01 2014

@author: Jeffrey
"""

class Problem7:
    
    def patternMatching(self,pattern,text):
        '''Given k-mer, pattern, and string, text,
        output all starting indices where pattern appears in text'''
        k = len(pattern)
        out = []
        for i in range(len(text)-k+1):
            if text[i:i+k] == pattern:
                out.append(i)

        return out
        
if __name__ == "__main__":
    p7 = Problem7()
    
    in_file = open("rosalind_1ccc.txt",'r')
    seq1 = in_file.readline()
    seq2 = in_file.readline()
    seq1 = seq1[:len(seq1)-1]
    seq2 = seq2[:len(seq2)-1]
    out_file = open("prob7_out.txt",'w')
    
    for index in p7.patternMatching(seq1,seq2):
        out_file.write(str(index)+" ")
    out_file.flush()