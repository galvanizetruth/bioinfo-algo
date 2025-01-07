# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 00:18:54 2014

@author: Jeffrey
"""

import time, sys

class Problem34:
    
    def overlap(self,patterns):
        output = []
        for i in range(len(patterns)):
            for j in range(len(patterns)):
                if i != j and patterns[i][1:] == patterns[j][:len(patterns[j])-1]:
                    edge = patterns[i]+" -> "+patterns[j]
                    if edge not in output:
                        output.append(edge)
        output.sort()
        return output
        
if __name__ == "__main__":
    p34 = Problem34()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_4b",'r')
    line = in_file.readline().strip()
    
    kmers = []
    while line and line != "":
        kmers.append(line)
        line = in_file.readline().strip()
    
    out_file = open("prob34_out.txt",'w')
    
    
    out = p34.overlap(kmers)

    for s in out:
        print s
        out_file.write(s+"\n")
    out_file.flush()
    
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"