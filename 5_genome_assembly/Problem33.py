# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 23:55:23 2014

@author: Jeffrey
"""

import time, sys

class Problem33:
    
    def composition(self,k,text):
        kmers = []
        for i in range(len(text)-k+1):
            kmers.append(text[i:i+k])
        kmers.sort()
        return kmers
        
if __name__ == "__main__":
    p33 = Problem33()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_4a.txt",'r')
    k = int(in_file.readline().strip())
    seq = in_file.readline().strip()
    
    out_file = open("prob33_out.txt",'w')
    
    
    kmers = p33.composition(k,seq)

    for kmer in kmers:
        print kmer
        out_file.write(kmer+"\n")
    out_file.flush()
    
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"