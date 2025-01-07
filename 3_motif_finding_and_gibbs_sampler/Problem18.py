# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 22:59:35 2014

@author: Jeffrey
"""


import time, random

class Problem18:
    
    def iterateRandMotifSearch(self,dna,k,numtimes):
        '''Iterates through randomizedMotifSearch numtimes, checking
        to see if bestMotifs has improved in score each time'''
        bestMotifs = []
        for first in dna:
            bestMotifs.append(first[:k])
        motifs = ["" for x in range(len(dna))]
        for i in range(numtimes):
            motifs = self.randomizedMotifSearch(dna,k)
            if self.findScore(motifs) < self.findScore(bestMotifs):
                bestMotifs = motifs[:]
        return bestMotifs
    
    def randomizedMotifSearch(self,dna,k):
        '''Starts at a random motif in dna and iterates by constructed a
        profile out of the motif, finding the profile-most probable kmer
        of each sequence, and checking the score of the new motif. If it
        has improved, then continue to iterate. If not, then stop.'''
        motifs = []
        for m in dna:
            randIndex = random.randint(0,len(m)-k)
            motifs.append(m[randIndex:randIndex+k])
        count = 0
        bestMotifs = motifs[:]
        while True:
            count += 1
            pro = self.profile(motifs)
            motifs = self.motifs(pro,dna)
            if self.findScore(motifs) < self.findScore(bestMotifs):
                bestMotifs = motifs[:]
            else:
                print count
                return bestMotifs
    
    def profile(self,motifs):
        '''Constructs the profile from a list of motifs, using pseudocounts'''
        counts = [[1 for x in range(4)] for x in range(len(motifs[0]))]
        bases = {'A':0,'C':1,'G':2,'T':3}
        for m in motifs:
            for i in range(len(m)):
                counts[i][bases[m[i]]] += 1
        freqs = []
        for pos in counts:
            total = float(sum(pos))
            freqs.append(map(lambda x: x / total,pos))
        return freqs
        
    def motifs(self,profile,dna):
        '''Constructs all of the profile-most probable kmers given a profile
        and a sequence, dna, returning a motif'''
        kmers = []
        for i in range(len(dna)):
            kmers.append(self.profileProbKMer(dna[i],len(profile),profile))

        return kmers
    
    def profileProbKMer(self,text,k,profile):
        '''Given a profile and a sequence and k, returns the profile-most
        probable kmer in the text'''
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
    
    def findScore(self,motifs):
        '''Returns the total hamming distance from the consensus sequence'''
        scores = [{'A':0,'C':0,'G':0,'T':0} for x in range(len(motifs[0]))]
        for i in range(len(motifs)):
            for j in range(len(motifs[i])):
                scores[j][motifs[i][j]] += 1
        
        out = 0
        for d in scores:
            maxKey = 'A'
            for key in d:
                if d[key] > d[maxKey]:
                    maxKey = key
            d.pop(maxKey)
            out += sum(d.values())
        return out
    
if __name__ == "__main__":
    p18 = Problem18()
    start_time = time.time()
    in_file = open("rosalind_3ff.txt",'r')
    nums = in_file.readline().strip().split(" ")
    k = int(nums[0])
    t = int(nums[1])
    
    dna = []
    line = in_file.readline().strip()
    while line and line != "":
        dna.append(line)
        line = in_file.readline().strip()
    out_file = open("prob18_out.txt",'w')
    print k,t
    
    motif = p18.iterateRandMotifSearch(dna,k,1000)
    print p18.findScore(motif)
    for kmer in motif:
        print kmer
        out_file.write(kmer+"\n")
    print '\n',
    out_file.flush()
    print time.time() - start_time, "seconds"