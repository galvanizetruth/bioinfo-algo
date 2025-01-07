# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 13:36:02 2014

@author: Jeffrey
"""

import time, random, numpy as np

class Problem19:
    
    def iterateGibbsSampler(self,dna,k,t,n,numtimes):
        '''Iterate through gibbsSampler numTimes, starting with the first
        kmer in each sequence as bestMotifs and running gibbsSampler on 
        random starts numtimes times, saving the motif if it improved'''
        bestMotifs = []
        for first in dna:
            bestMotifs.append(first[:k])
        motifs = ["" for x in range(t)]
        for i in range(numtimes):
            motifs = self.gibbsSampler(dna,k,t,n)

            if self.findScore(motifs) < self.findScore(bestMotifs):
                bestMotifs = motifs[:]
        return bestMotifs
    
    def gibbsSampler(self,dna,k,t,n):
        '''Given a set of t sequences, dna, a k, and n for the number of times
        to iterate, return the bestMotif after randomly selecting a kmer from
        motifs, removing it, constructing a profile, and then sampling kmers
        from the sequence missing at a rate equal to the probability of that
        kmer given the profile.'''
        motifs = []
        #Randomly initialize motifs
        for m in dna:
            randIndex = random.randint(0,len(m)-k)
            motifs.append(m[randIndex:randIndex+k])
        
        #Iterate n times
        bestMotifs = motifs[:]
        for i in range(n):
            #Randomly choose an index to remove from motifs from seq[i]
            index = random.randint(0,t-1)
            #Make a profile out of the other motifs
            pro = self.profile(motifs[0:index]+motifs[index+1:len(motifs)])
            #Get the probabilities of each kmer in seq[i]
            probs = self.profProbKMer(dna[index],k,pro)
            #Choose a random kmer out of those probabilities
            new_k_index = self.random(probs)
            motifs[index] = dna[index][new_k_index:new_k_index+k]
            #Check the score of the new set of motifs
            if self.findScore(motifs) < self.findScore(bestMotifs):
                bestMotifs = motifs[:]
                
        return bestMotifs
            
    def profProbKMer(self,text,k,profile):
        '''Given a profile and a sequence and a k, return the probability
        of each kmer in text based on the profile'''
        bases = {'A':0,'C':1,'G':2,'T':3}
        probs = []
        
        for i in range(len(text)-k+1):
            kmer = text[i:i+k]
            p = 1
            for j in range(len(profile)):
                p *= profile[j][bases[kmer[j]]]
            probs.append(p)
            
        #Note: probs[i] == prob of the kmer at text[i:i+k]
        return probs
    
    def profile(self,motifs):
        '''Given a set of motifs, return the profile matrix of the
        probability of getting each base at each position in motifs'''
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
        
    def random(self,probs):
        '''Given a list of probabilities, return the index of the
        one that was sampled randomly from a uniform distribution'''
        cutoffs = np.cumsum(probs)
        return cutoffs.searchsorted(np.random.uniform(0,cutoffs[-1]))
        
    
    '''def random(self,p_array):
        total = sum(p_array)
        r = random.random()
        for i in range(len(p_array)):
            r -= p_array[i] / total
            if(r <= 0):
                return i
        return len(p_array)-1'''
    
    def findScore(self,motifs):
        '''Given a set of motifs, return the total hamming distance
        between the motifs and the consensus sequence'''
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
    p19 = Problem19()
    
    start_time = time.time()
    in_file = open("rosalind_3hh.txt",'r')
    nums = in_file.readline().strip().split(" ")
    k = int(nums[0])
    t = int(nums[1])
    n = int(nums[2])
    
    dna = []
    line = in_file.readline().strip()
    while line and line != "":
        dna.append(line)
        line = in_file.readline().strip()
    out_file = open("prob19_out.txt",'w')
    
    motif = p19.iterateGibbsSampler(dna,k,t,n,20)
    print p19.findScore(motif)
    for kmer in motif:
        print kmer
        out_file.write(kmer+"\n")
    
    print '\n',
    out_file.flush()
    print time.time() - start_time, "seconds"