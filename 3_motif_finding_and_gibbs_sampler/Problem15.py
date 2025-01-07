# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:11:21 2014

@author: Jeffrey
"""

import time

class Problem15:
    
    def profileProbKMer(self,text,k,profile):
        '''Given a profile matrix of probabilities, a k, and a text,
        Return the kmer in text that has the highest probability given profile'''
        bases = {'A':0,'C':1,'G':2,'T':3}
        #Probs gives the probability of each kmer in text
        probs = {}
        maxProb = 0
        maxKMer = ""
        
        for i in range(len(text)-k+1):
            kmer = text[i:i+k]
            p = 1
            for j in range(k):
                p *= profile[j][bases[kmer[j]]]
            probs[kmer] = p
            
            if p >= maxProb:
                maxProb = p
                maxKMer = kmer
        return maxKMer
        
        
        
if __name__ == "__main__":
    p15 = Problem15()
    start_time = time.time()
    in_file = open("rosalind_3c.txt",'r')
    text = in_file.readline().strip()
    k = int(in_file.readline().strip())
    
    mat = []
    for i in range(k):
        line = in_file.readline().strip()
        row = []
        for num in line.split(" "):
            row.append(float(num))
        mat.append(row)
    out_file = open("prob15_out.txt",'w')
    
    kmer = p15.profileProbKMer(text,k,mat)
    print kmer
    out_file.write(kmer)
    out_file.flush()
    print time.time() - start_time, "seconds"