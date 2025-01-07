# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 22:00:38 2014
    
@author: Jeffrey
"""

import sys,time

class Problem47:
    
    def longestSharedSubstringHash(self,text1,text2):
        k = 2
        output = ""
        while k < len(text1):
            substrings = {}
            exists = False
            for i in range(len(text1)-k+1):
                substrings[text1[i:i+k]] = 1
            for i in range(len(text2)-k+1):
                if substrings.has_key(text2[i:i+k]):
                    output = text2[i:i+k]
                    exists = True
                    break
            if not exists:
                return output
            k += 1
        return output
    
    def localAlignment(self,seq1,seq2):
        gap = inf
        scores = [[0 for x in range(len(seq2)+1)] for x in range(len(seq1)+1)]
        backtrack = [[-1 for x in range(len(seq2)+1)] for x in range(len(seq1)+1)]
        for i in range(1,len(seq1)+1):
            scores[i][0] = scores[i-1][0] - gap
        for j in range(1,len(seq2)+1):
            scores[0][j] = scores[0][j-1] - gap
        for i in range(1,len(seq1)+1):
            for j in range(1,len(seq2)+1):
                match = -inf
                if seq1[i-1] == seq2[j-1]:
                    match = 1
                scores[i][j] = max(scores[i-1][j]-gap,scores[i][j-1]-gap,scores[i-1][j-1]+match,0)

                if scores[i][j] == scores[i-1][j]-gap:
                    backtrack[i][j] = 2
                elif scores[i][j] == scores[i][j-1]-gap:
                    backtrack[i][j] = 1
                elif scores[i][j] == scores[i-1][j-1]+match:
                    backtrack[i][j] = 0
                elif scores[i][j] == 0:
                    backtrack[i][j] = -1

        maxI = len(seq1)
        maxJ = len(seq2)
        maxScore = 0
        for i in range(len(seq1)+1):
            for j in range(len(seq2)+1):
                if scores[i][j] > maxScore:
                    maxScore = scores[i][j]
                    maxI = i
                    maxJ = j

        i = maxI
        j = maxJ
        out1 = ""
        out2 = ""
        while i != 0 and j != 0 and backtrack[i][j] != -1:
            if backtrack[i][j] == 2:                
                out1 = seq1[i-1] + out1
                out2 = "-" + out2
                i = i-1
            elif backtrack[i][j] == 1:
                out1 = "-" + out1
                out2 = seq2[j-1] + out2
                j = j-1
            else:
                out1 = seq1[i-1] + out1
                out2 = seq2[j-1] + out2
                i = i-1
                j = j-1

        return out1

    def longestSharedTrie(self,patterns1,patterns2):
        trie = {}
        currI = 0
        newI = 1
        long_rep = ''
        for kmer in patterns1:
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
            
        for kmer in patterns2:
            for depth,s in enumerate(kmer):
                if trie and currI in trie:
                    if depth > len(long_rep):
                        long_rep = kmer[:depth]
                    foundBase = False
                    for (i,base) in trie[currI]:
                        if s == base:
                            currI = i
                            foundBase = True
                    if not foundBase:
                        currI = -1
                else:
                    break
            currI = 0
        return trie,long_rep
    
    def makeSuffixTrie(self,text1,text2):
        patterns1 = []
        for i in range(len(text1)):
            patterns1.append(text1[i:])
        patterns2 = []
        for i in range(len(text2)):
            patterns2.append(text2[i:])
        return self.longestSharedTrie(patterns1,patterns2)
    

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
    p47 = Problem47()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_7e2.txt",'r')
    text1 = in_file.readline().strip()
    text2 = in_file.readline().strip()
    print len(text1)
    print len(text2)
    '''
    line = in_file.readline().strip()

    kmers = []
    while line and line != "":
        kmers.append(line)
        line = in_file.readline().strip()'''
    
    out_file = open("prob47_out.txt",'w')
    trie,out = p47.makeSuffixTrie(text1,text2)
    #out = p47.longestSharedSubstringHash(text1,text2)
    print out
    out_file.write(out)
    out_file.flush()
    
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"