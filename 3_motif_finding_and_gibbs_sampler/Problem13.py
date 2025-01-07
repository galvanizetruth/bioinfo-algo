# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 20:56:17 2014

@author: Jeffrey
"""
import time

class Problem13:
    
    def motifEnumeration(self,k,d,texts):
        '''Given a collection of sequences, texts, a k, and a d max mismatches,
        Return all k-mers that appear in all texts with at most d mismatches'''
        #Use a set to ensure unique kmers
        kmers = set()
        for i in range(len(texts[0])-k+1):
            #Add all inexactMatches of each kmer in texts[0] to kmers
            for seq in self.inexactMatches(texts[0][i:i+k],d,0):
                kmers.add(seq)
        #For the rest of the texts,
        for i in range(1,len(texts)):
            out = set()
            for j in range(len(texts[i])-k+1):
                #Compare each kmer with the current one in text
                #and see if it inexactlyMatches. If so, add it to the output
                for seq in kmers:
                    if self.approxMismatch(seq,texts[i][j:j+k],d):
                        out.add(seq)
            #Only keep the kmers that are in both out and kmers
            kmers = kmers.intersection(out)        
        return list(kmers)
        
    def inexactMatches(self,seq,d,i):
        '''Returns all kmers with at most d mismatches from seq'''
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
        
    def approxMismatch(self,seq1,seq2,d):
        '''Returns true if seq1 == seq2 with at most d mismatches'''
        for c1,c2 in zip(seq1,seq2):
            if c1 != c2:
                if d == 0:
                    return False
                else:
                    d -= 1
        return True

if __name__ == "__main__":
    p13 = Problem13()
    start_time = time.time()
    in_file = open("rosalind_3aa.txt",'r')
    nums = in_file.readline()
    nums = nums.split(" ")
    k = int(nums[0])
    d = int(nums[1])
    seqs = []
    line = in_file.readline().strip()
    while line and line !="":
        seqs.append(line)
        line = in_file.readline().strip()
    out_file = open("prob13_out.txt",'w')
    
    for kmer in p13.motifEnumeration(k,d,seqs):
        print kmer,
        out_file.write(kmer+" ")
    out_file.flush()
    print time.time() - start_time, "seconds"