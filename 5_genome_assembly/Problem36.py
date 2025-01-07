# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:04:52 2014

@author: Jeffrey
"""


import time, sys

class Problem36:
    
    def deBruijnKmer(self,kmers):
        graph = {}
        for kmer in kmers:
            if not graph.has_key(kmer[:-1]):
                graph[kmer[:-1]] = [kmer[1:]]
            else:
                graph[kmer[:-1]].append(kmer[1:])
            
        printout = []
        for key in graph:
            edges = key + " -> "
            graph[key].sort()
            for dest in graph[key]:
                edges += dest+","
            printout.append(edges[:-1])
        printout.sort()
        return printout
        
if __name__ == "__main__":
    p36 = Problem36()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_4ddd.txt",'r')
    line = in_file.readline().strip()
    
    kmers = []
    while line and line != "":
        kmers.append(line)
        line = in_file.readline().strip()
    
    out_file = open("prob36_out.txt",'w')
    
    
    out = p36.deBruijnKmer(kmers)

    for s in out:
        print s
        out_file.write(s+"\n")
    out_file.flush()
    
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"