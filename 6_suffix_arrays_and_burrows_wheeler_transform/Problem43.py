# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 21:22:13 2014

@author: Jeffrey
"""

import time,sys

class Problem43:
    
    def makeTrie(self, patterns):
        trie = {}
        currI = 0
        newI = 1
        for kmer in patterns:
            for s in kmer:
                if trie and trie.has_key(currI):
                    foundBase = False
                    for (i,base) in trie[currI]:
                        if s == base:
                            currI = i
                            foundBase = True
                    if not foundBase:
                        trie[currI].append((newI,s))
                        currI = newI
                        newI += 1
                else:
                    trie[currI] = [(newI,s)]
                    currI = newI
                    newI += 1
            currI = 0
        return trie
        
        
if __name__ == "__main__":
    p43 = Problem43()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_7a4.txt",'r')
    line = in_file.readline().strip()

    kmers = []
    while line and line != "":
        kmers.append(line)
        line = in_file.readline().strip()
    
    out_file = open("prob43_out.txt",'w')
    out = p43.makeTrie(kmers)

    for key in out:
        for (i,base) in out[key]:
            print str(key)+'->'+str(i)+':'+base
            out_file.write(str(key)+'->'+str(i)+':'+base+'\n')
    out_file.flush()
    
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"