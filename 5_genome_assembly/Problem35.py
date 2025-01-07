# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:35:44 2014

@author: Jeffrey
"""


import time, sys

class Problem35:
    
    def deBruijn(self,k,text):
        output = {}
        for i in range(len(text)-k+1):
            kmer = text[i:i+k]
            if not output.has_key(kmer[:k-1]):
                output[kmer[:k-1]] = [kmer[1:]]
            else:
                output[kmer[:k-1]].append(kmer[1:])
            
        printout = []
        for key in output:
            edges = key + " -> "
            output[key].sort()
            for dest in output[key]:
                edges += dest+","
            printout.append(edges[:-1])
        printout.sort()
        return printout
        
if __name__ == "__main__":
    p35 = Problem35()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_4c.txt",'r')
    k = int(in_file.readline().strip())
    text = in_file.readline().strip()

    
    out_file = open("prob35_out.txt",'w')
    
    
    out = p35.deBruijn(k,text)

    for s in out:
        print s
        out_file.write(s+"\n")
    out_file.flush()
    
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"