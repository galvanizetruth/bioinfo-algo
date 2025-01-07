# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 19:07:16 2014

@author: Jeffrey
"""

import time

class Problem16:
    
    def greedyMotifSearch(self,k,t,dna):
        '''Given t sequences in dna, and a k, apply greedyMotifSearch,
        starting at each kmer in the first sequence of dna, make profiles
        out of each additional kmer added and find the profileProbKMer
        at each step, maximizing the score of the overall motif at the end'''
        #Note: a motif is a collection of t k-mers, one from each seq in dna
        
        #Initialize bestMotifs with the first kmer of each seq
        bestMotifs = []
        for first in dna:
            bestMotifs.append(first[:k])
        motifs = ["" for x in range(t)]
        for x in range(len(dna[0])-k+1):
            motifs[0] = dna[0][x:x+k]
            for i in range(1,t):
                profile = self.makeProfile(motifs[0:i])
                motifs[i] = self.profileProbKMer(dna[i],k,profile)
            
            if self.findScore(motifs) < self.findScore(bestMotifs):
                bestMotifs = motifs[:]
        
        return bestMotifs
                
    def findScore(self,motifs):
        '''Given a motif, returns the score of them summing the scores of the
        bases that differ from the consensus'''
        #Count how many of each base are at each position in motifs
        scores = [{'A':0,'C':0,'G':0,'T':0} for x in range(len(motifs[0]))]
        for i in range(len(motifs)):
            for j in range(len(motifs[i])):
                scores[j][motifs[i][j]] += 1
        
        out = 0
        #Find the base that occurs the most at each position, remove that
        #count, and sum the rest of the counts, giving scores for each base
        for d in scores:
            maxKey = 'A'
            for key in d:
                if d[key] > d[maxKey]:
                    maxKey = key
            d.pop(maxKey)
            out += sum(d.values())
        return out
    
    def makeProfile(self,motifs):
        '''Given a set of motifs, create a profile matrix with the
        probabilities of getting each base at each position in motifs'''
        counts = [[0 for x in range(4)] for x in range(len(motifs[0]))]
        bases = {'A':0,'C':1,'G':2,'T':3}
        #Count up how many of each base occur at each position
        for m in motifs:
            for i in range(len(m)):
                counts[i][bases[m[i]]] += 1
        #Turn counts into frequencies
        freqs = []
        for pos in counts:
            total = float(sum(pos))
            freqs.append(map(lambda x: x / total,pos))
        return freqs
    
    def profileProbKMer(self,text,k,profile):
        '''Given a profile, a sequence, text, and a k, find the profile-most
        probably kmer in the text'''
        bases = {'A':0,'C':1,'G':2,'T':3}
        probs = {}
        maxProb = 0
        maxKMer = text[:k]
        
        for i in range(len(text)-k+1):
            kmer = text[i:i+k]
            p = 1
            for j in range(len(profile)):
                p *= profile[j][bases[kmer[j]]]
            probs[kmer] = p
            
            if p > maxProb:
                maxProb = p
                maxKMer = kmer
        return maxKMer    
        
if __name__ == "__main__":
    p16 = Problem16()
    start_time = time.time()
    in_file = open("rosalind_3dddd.txt",'r')
    nums = in_file.readline().strip().split(" ")
    k = int(nums[0])
    t = int(nums[1])
    
    dna = []
    line = in_file.readline().strip()
    while line and line != "":
        dna.append(line)
        line = in_file.readline().strip()
    out_file = open("prob16_out.txt",'w')
    
    for kmer in p16.greedyMotifSearch(k,t,dna):
        print kmer,
        out_file.write(kmer+" ")
    print '\n',
    out_file.flush()
    print time.time() - start_time, "seconds"