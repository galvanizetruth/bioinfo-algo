# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:42:11 2014

@author: Jeffrey
"""

class Problem10:
    
    def apprPatternMatching(self,pattern,text,d):
        '''Given a kmer, pattern, and a sequence, text,
        Output the positions in text where pattern appears with <= d mismatches'''
        k = len(pattern)
        out = []
        for i in range(len(text)-k+1):
            if self.approxMismatch(text[i:i+k],pattern,d):
                out.append(i)
        return out
        
    def approxMismatch(self,seq1,seq2,d):
        '''Given two k-mers, seq1+seq2, return True if they are at most d
        mismatches different. Do this recursively'''
        for c1,c2 in zip(seq1,seq2):
            if c1 != c2:
                if d == 0:
                    return False
                else:
                    d -= 1
        return True
        
if __name__ == "__main__":
    p10 = Problem10()
    
    in_file = open("rosalind_1f.txt",'r')
    seq1 = in_file.readline().strip()
    seq2 = in_file.readline().strip()
    d = int(in_file.readline())
    out_file = open("prob10_out.txt",'w')
    
    for index in p10.apprPatternMatching(seq1,seq2,d):
        out_file.write(str(index)+" ")
    out_file.flush()