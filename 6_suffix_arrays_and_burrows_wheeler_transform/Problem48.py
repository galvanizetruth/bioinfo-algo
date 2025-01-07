# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 13:23:55 2014

@author: Jeffrey
"""


import sys,time

class Problem48:
    
    def shortestNonSharedSubstringHash(self,text1,text2):
        k = 2
        output = ""
        while k < len(text2):
            substrings = {}
            for i in range(len(text2)-k+1):
                substrings[text2[i:i+k]] = 1
            for i in range(len(text1)-k+1):
                kmer = text1[i:i+k]
                if not substrings.has_key(kmer):
                    return kmer
            k += 1
        return output


    def shortestNonsharedTrie(self,patterns1,patterns2):
        trie = {}
        currI = 0
        newI = 1
        short_non = patterns1[0]
        for kmer in patterns2:
            for depth,s in enumerate(kmer):
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
            
        for kmer in patterns1:
            for depth,s in enumerate(kmer):
                if trie and currI in trie:
                    foundBase = False
                    for (i,base) in trie[currI]:
                        if s == base:
                            currI = i
                            foundBase = True
                    if not foundBase:
                        if depth < len(short_non):
                            short_non = kmer[:depth+1]
                        currI = -1
                else:
                    break
            currI = 0
        return trie,short_non
    
    def makeSuffixTrie(self,text1,text2):
        patterns1 = []
        for i in range(len(text1)):
            patterns1.append(text1[i:])
        patterns2 = []
        for i in range(len(text2)):
            patterns2.append(text2[i:])
        return self.shortestNonsharedTrie(patterns1,patterns2)

    
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
    p48 = Problem48()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_7f2.txt",'r')
    text1 = in_file.readline().strip()
    text2 = in_file.readline().strip()
    #print len(text1)
    #print len(text2)
    '''
    line = in_file.readline().strip()

    kmers = []
    while line and line != "":
        kmers.append(line)
        line = in_file.readline().strip()'''
    
    out_file = open("prob48_out.txt",'w')
    trie,out = p48.makeSuffixTrie(text1,text2)
    #out = p48.shortestNonSharedSubstringHash(text1,text2)
    print out
    out_file.write(out)
    out_file.flush()
    
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"