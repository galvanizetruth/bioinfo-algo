# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 16:28:37 2014

@author: Jeffrey
"""


import time,sys

class Problem44:
    
    def multPattMatch(self,text,patterns):
        trie = self.makeTrie(patterns)
        outI = []
        for i in range(len(text)):
            currNode = 0
            currI = i
            inTrie = True
            while trie.has_key(currNode) and currI < len(text) and inTrie:
                foundBase = False
                for (node,base) in trie[currNode]:
                    if currI < len(text) and text[currI] == base:
                        foundBase = True
                        currI += 1
                        currNode = node
                        break

                inTrie = foundBase
            if not trie.has_key(currNode):
                outI.append(i)
                        
        return outI
    
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
    p44 = Problem44()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_7b2.txt",'r')
    text = in_file.readline().strip()
    line = in_file.readline().strip()

    kmers = []
    while line and line != "":
        kmers.append(line)
        line = in_file.readline().strip()
    
    out_file = open("prob44_out.txt",'w')
    out = p44.multPattMatch(text,kmers)

    for i in out:
        print i,
        out_file.write(str(i)+' ')
    out_file.flush()
    
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"