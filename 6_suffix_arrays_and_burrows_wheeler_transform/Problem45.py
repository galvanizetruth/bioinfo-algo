# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 13:46:13 2014

@author: Jeffrey
"""


import time,sys

class Problem45:
    
    def longestRepeat(self,text):
        trie = self.makeSuffixTrie(text)
        #print trie
        nodesToVisit = [0]
        nodeStrings = ['']
        outputStrings = []
        while nodesToVisit:
            currNode = nodesToVisit.pop()
            currString = nodeStrings.pop()
            if trie.has_key(currNode):
                if len(trie[currNode]) > 1:
                    outputStrings.append(currString)
                for (i,base) in trie[currNode]:
                    nodesToVisit.append(i)
                    nodeStrings.append(currString + base)
                #print nodesToVisit
                #print nodeStrings
        #print outputStrings
        maxLen = 0
        maxStr = ""
        for s in outputStrings:
            if len(s) > maxLen:
                maxLen = len(s)
                maxStr = s
        return maxStr
    
    def longestRepeatTrie(self,patterns):
        trie = {}
        currI = 0
        newI = 1
        nodes = {}
        long_rep = ''
        for kmer in patterns:
            for depth,s in enumerate(kmer):
                if currI not in nodes:
                    nodes[currI] = (1,depth)
                else:
                    nodes[currI] = (nodes[currI][0]+1,depth)
                
                if nodes[currI][0] > 1 and depth > len(long_rep):
                    long_rep = kmer[:depth]
                    
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
        return trie,long_rep
        
    def makeSuffixTrie(self,text):
        patterns = []
        for i in range(len(text)):
            patterns.append(text[i:]+"$")
        return self.longestRepeatTrie(patterns)
    
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
    
    def longestRepeatHash(self,text):
        k = 2
        output = ""
        while k < len(text):
            substrings = {}
            exists = False
            for i in range(len(text)-k+1):
                kmer = text[i:i+k]
                if substrings.has_key(kmer):
                    output = kmer
                    exists = True
                    break
                else:
                    substrings[kmer] = 1
            if not exists:
                return output
            k += 1
        return output
    
    def longestRepeatBruteForce(self,text):
        k = len(text)-1
        while k > 0:
            substrings = []
            for i in range(len(text)-k+1):
                kmer = text[i:i+k]
                if kmer in substrings:
                    return kmer
                else:
                    substrings.append(kmer)
            k -= 1
        return ""
        
        
if __name__ == "__main__":
    p45 = Problem45()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_7ctest.txt",'r')
    #text = in_file.readline().strip()
    text = "GGGTCCACATGGTGATATGTTTACCGGTAGGGAGCGGGTAACCGCCTATGCTTCGTTACCATCACCTCCCGTAGCCCCCAGTCATTTTACGGAAGGGGCCCGGGATCCGGGCATACTCGGGTCACTCCTACGATGAGAATTCGATCAGGATATTCCAAGTAGAGAACGCAATAAACTGACCTCATCATTTACTAGACATGATGTAGAAGAGCAGATGAGACAGAAGGGAGGCGCCTCATACGAGACTGTGTCTTCCTTTCCCGCCGGAAGCACCTAGACGGCTACATCTCTCTCGGCGCAGCATTACGAGATGTGATACGGCCGATAGAACACTGCGGTCCAATTACATCATTATCCTAATTAACATATTGCGCTCCTGGTCGTTAGATATCCCGCACACTATAGGAAGAGGAGAGACTCACTTGACTTAGCCAGGTAACAGCATGACACACGCAGACGCGCTCCCTATGGGGGCCATGCGCTCCATACAATCCAGGGTGCAAAGAGTTATAACGAACAGACCGGATTTCCGTTCCAGCAGAGGAAGGCAGTCAATAGTCTACCGTAACGGTTATAAGTGGGCGTCCGATGTCTCCAATGGTTCGACCGAACCGGGCATGTGGCGCACCATTTGTCTTACCTTAACGTGACCAGACGAATCCGCATGAACTTTCCTGGACAATTGAGCGAGTCCAGTGAGTAAACAACCACAGCAGATACTATACCGAGGCGAAATTGGGATCGGCCAGTACCCCGCGACGGATAGTCATCCATACAATCCAGGGTGCAAAGAGTTATAACGAACAGACCGGATTTCCGTTCCAGCAGAGGAAGGCAGTCAATAGTCTACCGACTATCGTATCCGCAGCGTAACTTGGCCAGTGCGATCTACATAGCTGACGAGCATCCTTGGGTCCTATGTATGACTGTACGGTCTATGAAATACCTTTTGTCGATCGTCCACCACTTTAAGTGTGGCAGGCATGGTTGTGTCTCATCAACCGACGTTTCGACCCCCCGGTGTCGCTAAAGCGGCGCGTTTAACCTCTGATTCGAGACCTGACACATTCCATGAAGGTGGGTCGCAAGGTGAACAAAATGGCCGAATATGACTTCTGCCGGTTAAGGTAGTACGGTCAAAGTGCACCCGTTGCTCGCGGCATCTACGCTCGCTGCAAATCACAGCTCTTTCTCTTCGTGCCTGAGCCGTTGCCAGATCGGGGTCGATCAGCTCACGCATGATGCGTGTACCCACACCGTCTCTTGTAGCGTCGCTGACTTGTCGATCATACTAACACGATCTTGCCTCCATACAATCCAGGGTGCAAAGAGTTATAACGAACAGACCGGATTTCCGTTCCAGCAGAGGAAGGCAGTCAATAGTCTACCGTGGGATGAGTCAGACTTGACGTTAGTGAGGAAACCAAAACATTTCCTGACCCAACACGCGTTGGGCAGTGTACCCGTGCGTTGTGCTGCTACTGGCACTACGCCATTATAATTACCTTGCCAGTTAGCTCGCGGCACTAATGTTTAGAAGGTTCACGTACCCGGTTACATACCGGGGTTCACCTCGCATTCCCTCACCCTAGACCAGTTCAGACGATCTTCGGCATCCGCCCCGGCGCCGGGGATATTCACCCAGTAGTAAGCCCCGGCTTCTTTACTCTGCGACCTAACACCCTGTCCTTCCTTCGCGCAGTTGAGGAACGCTTGACGTCGATACATTGCACAGGGTGCTCTACGGAACACAATCAGCCACTACTGAATTAAGACCTTTACAGACGACATCACAGTCATACCAGGTGAAATTTGGGGAGAATAGTTAACCTGCCTCATACTCAAATCATAGAATGGACTACATATCCAGCACGGGCTACTGACCCGCAGGTATACTAATCAGAGGCATTTGCGTCATCGATGTACTTTCAACATAGCATAAAGATACGAGCGCCAAGTGGGATCGCGCCAAGCTACTGTCTGTGCTTAGCGTAACGTTATTACGAGAATCTAAAAGCGCCTATGTTCTATTTACTAACAGTGCCTTTAAGCTAGCGTAACGCCTGACGCTTCTCCCATTTCGGGGTATTAGATACCAGACCATTAAGTAGTGCCCCCTAACATTTTTCCGCGCGAGTTTCTCAGAGGATCGACGAGGAGGAACACGACTCGGCGAGCAACGATGGAGTCCGGCACGGAGTAGTTAACGGGCCATCCAGCAAGGGATCAGAGGTTCCTCTGCTATGGTCTCCGTCTCAGCTCCGATACTAGCTCGTCCAACGACGATTACCCTTCAAGGGAAGTGAGGTACCTCTTAAAGAAAATTGCGTCGCTCAAGAGATGGGTATGGCCCCGGGGAGTAGTACACAAGGAGTATTATCGTAAATCTAGTATTGCTAAGGGTGGCTATGAAATGACTTTCTTATGGGGCATGAACTTAACCCGAGTAAGGACAAAATTGCTCACATGGGGACCCCTCATCGCCCTGCTTATTTTGTTGCGGTTTATGTTCCTCTAGTGGCCCTAGAAGTGCCTGAGGCTGGACCAAATGGCCGTAGCTGCGCCATTCCAGCCATCACTCCTGACCGCGAGGCCAGGGAACGCTCGTGCCCCTATTTATTCTAACCGCAATCGAGCTACCGGCCATGGCCCACGTCCCTTAGAATTCTGATGTTTATGCGTGCCGTGCCGGAGAGATCGCAAAAGAAAGAGCAGTCTCTCTGATCTTCAGCGCCGCTTGTCCCAACCC"
    '''
    line = in_file.readline().strip()

    kmers = []
    while line and line != "":
        kmers.append(line)
        line = in_file.readline().strip()'''
    
    out_file = open("prob45_out.txt",'w')
    trie,out = p45.makeSuffixTrie(text)

    #for i in out:
    print out,
    out_file.write(str(out)+' ')
    out_file.flush()
    
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"