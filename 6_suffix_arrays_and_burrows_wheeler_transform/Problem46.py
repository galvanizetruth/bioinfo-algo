# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:17:17 2014

@author: Jeffrey
"""

import sys,time

class Problem46:
    
    def makeSuffixTree(self,text):
        trie = self.makeSuffixTrie(text)
        tree = {}
        nodesToVisit = [1]
        while nodesToVisit:
            firstNode = nodesToVisit.pop()
            currParent = firstNode
            if trie.has_key(currParent):
                newNodes = []
                for (nextNode,child_base) in trie[currParent]:
                    childString = child_base
                    while trie.has_key(nextNode) and len(trie[nextNode]) == 1:
                        (i,base) = trie[nextNode][0]
                        nextNode = i
                        childString += base
                    newNodes.append((nextNode,childString))
                    if trie.has_key(nextNode):
                        nodesToVisit.append(nextNode)
                tree[currParent] = newNodes
            
        #print tree
        return tree
    
    def makeSuffixTrie(self,text):
        patterns = []
        for i in range(len(text)):
            patterns.append(text[i:])
        return self.makeTrie(patterns)
    
    def makeTrie(self, patterns):
        trie = {}
        currI = 1
        newI = 2
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
            currI = 1
        return trie
    
        
if __name__ == "__main__":
    p46 = Problem46()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_7d2.txt",'r')
    text = in_file.readline().strip()
    '''
    line = in_file.readline().strip()

    kmers = []
    while line and line != "":
        kmers.append(line)
        line = in_file.readline().strip()'''
    
    out_file = open("prob46_out.txt",'w')
    out = p46.makeSuffixTree(text)

    for i in out:
        for e in out[i]:
            print e[1]
            out_file.write(str(e[1])+'\n')
    out_file.flush()
    print len(text)
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"