# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 19:38:33 2014

@author: Jeffrey
"""

import time

class Problem12:
    
    def freqWordsMismatchRevComp(self,text,k,d):
        '''Given a text, a k, and a maximum of d mismatches,
        return the most frequent kmers in text with up to d mismatches
        including reverse complements'''
        freq_num = 0
        kmer_freqs = {}
        most_freq = []
        '''Same as previous problem but just append the revComp sequences
        and add the scores of the two together because they count as 1 kmer'''
        for i in range(len(text)-k+1):
            kmer = text[i:i+k]
            forward = self.inexactMatches(kmer,d,0)
            inexact = []
            for s in forward:
                inexact.append(s)
                inexact.append(self.revComp(s))
            for seq in inexact:
                if kmer_freqs.has_key(seq):
                    kmer_freqs[seq] += 1
                    
                    curr = kmer_freqs[seq] + kmer_freqs[self.revComp(seq)]
                    if curr > freq_num:
                        most_freq = []
                        freq_num = curr
                    if curr >= freq_num:
                        most_freq.append(seq)
                        most_freq.append(self.revComp(seq))
                else:
                    kmer_freqs[seq] = 1
        return most_freq
        
    def inexactMatches(self,seq,d,i):
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
        
    def revComp(self,string):
        out = ""
        for c in string:
            if c == "A":
                out += "T"
            elif c == "C":
                out += "G"
            elif c == "G":
                out += "C"
            elif c == "T":
                out += "A"
            else:
                pass
        return out[::-1]

if __name__ == "__main__":
    p12 = Problem12()
    start_time = time.time()
    in_file = open("rosalind_1hh.txt",'r')
    seq1 = in_file.readline().strip()
    nums = in_file.readline()
    nums = nums.split(" ")
    k = int(nums[0])
    d = int(nums[1])
    out_file = open("prob12_out.txt",'w')
    
    for kmer in p12.freqWordsMismatchRevComp(seq1,k,d):
        out_file.write(kmer+" ")
    out_file.flush()
    print time.time() - start_time, "seconds"