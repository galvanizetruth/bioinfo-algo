# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 20:56:17 2014

@author: Jeffrey
"""
import time

class Problem14:
    
    def medianString(self,k,texts):
        '''Given a set of seqs, texts, and a k, find one k-mer
        that exist in all of texts with the least number of mismatches, d'''
        d = 0
        out = ""
        minScore = len(texts[0])-k
        while minScore > d*len(texts):
            #Find all inexactMatches in texts[0] with difference d
            pats = []
            for i in range(len(texts[0])-k+1):
                pats += self.inexactMatches(texts[0][i:i+k],d,0)
            
            #find the hammingDistance between each kmer and each text
            #and sum them up, and output the lowest scoring kmers
            for kmer in pats:
                currScore = 0
                for seq in texts:
                    currScore += self.hammingDistance(kmer,seq)
                if currScore < minScore:
                    minScore = currScore
                    out = kmer
            d += 1
            
        return out
        
    def bruteForceMedianString(self,k,texts):
        '''Searches all kmers of length k and chooses the best scoring one'''
        bestPattern = "A"*k
        bestScore = 0
        for seq in texts:
            bestScore += self.hammingDistance(bestPattern,seq)
        for kmer in self.allKmers(k,[]):
            currScore = 0
            for seq in texts:
                currScore += self.hammingDistance(kmer,seq)
            if currScore < bestScore:
                bestScore = currScore
                bestPattern = kmer
        return bestPattern
        
    def allKmers(self,k,out):
        '''Returns all kmers of length k'''
        if out == []:
            return self.allKmers(k,['A','C','G','T'])
        else:
            if len(out[0]) == k:
                return out
            else:
                res = []
                bases = ['A','C','G','T']
                for s in out:
                    for b in bases:
                        res.append(s+b)
                return self.allKmers(k,res)
    
    def hammingDistance(self,kmer,seq):
        '''Given a kmer and a sequence, find the smallest hamming distance
        between the kmer and each kmer in the sequence'''
        d = len(kmer)
        for i in range(len(seq)-len(kmer)+1):
            numMis = 0
            for a,b in zip(kmer,seq[i:i+len(kmer)]):
                if a != b:
                    numMis += 1
            
            if numMis < d:
                d = numMis
        return d        
    
        
    def inexactMatches(self,seq,d,i):
        '''Generate all inexactMatches of seq with at most d mismatches'''
        if d == 0 or i == len(seq):
            return [seq]
        else:
            bases = ['A','C','G','T']
            out = []
            for b in bases:
                if seq[i] == b:
                    out += self.inexactMatches(seq,d,i+1)
                else:
                    out += self.inexactMatches(seq[:i]+b+seq[i+1:],d-1,i+1)
        return out        
        
if __name__ == "__main__":
    p14 = Problem14()
    start_time = time.time()
    in_file = open("rosalind_3bbbbb.txt",'r')
    nums = in_file.readline()
    #nums = nums.split(" ")
    k = int(nums[0])
    #d = int(nums[1])
    seqs = []
    line = in_file.readline().strip()
    while line and line !="":
        seqs.append(line)
        line = in_file.readline().strip()
    out_file = open("prob14_out.txt",'w')
    
    kmer = p14.bruteForceMedianString(k,seqs)
    #kmer = p14.medianString(k,seqs)
    print kmer,
    out_file.write(kmer)
    out_file.flush()
    print time.time() - start_time, "seconds"