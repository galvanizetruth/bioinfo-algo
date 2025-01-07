# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 22:48:18 2014

@author: Jeffrey
"""

class Problem11:
    
    def freqWordswMismatch(self,text,k,d):
        freq_num = 0
        kmer_freqs = {}
        inexact_kmers = {}
        most_freq = []
        for i in range(len(text)-k+1):
            kmer = text[i:i+k]
            if kmer_freqs.has_key(kmer):
                kmer_freqs[kmer][0] += 1
            else:
                if not inexact_kmers.has_key(kmer):
                    kmer_freqs[kmer] = [1,0]
                    for key in kmer_freqs:
                        if key != kmer and self.approxMismatch(kmer,key,d):
                            kmer_freqs[kmer][1] += kmer_freqs[key][0]
                else:
                    kmer_freqs[kmer] = [1,inexact_kmers.pop(kmer)]
            
            
            
            curr = kmer_freqs[kmer][0] + kmer_freqs[kmer][1]
            if curr > freq_num:
                most_freq = []
                freq_num = curr
            if curr >= freq_num:
                most_freq.append(kmer)
                

            for key in kmer_freqs:
                if key != kmer and self.approxMismatch(kmer,key,d):
                    kmer_freqs[key][1] += 1
                    
                    curr = kmer_freqs[key][0] + kmer_freqs[key][1]
                    if curr > freq_num:
                        most_freq = []
                        freq_num = curr
                    if curr >= freq_num:
                        most_freq.append(key)
                
        num = 0
        for key in kmer_freqs:
            if self.approxMismatch('AAAT',key,d):
                num += 1
        print num
        print kmer_freqs
        return most_freq_exist
    
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
    
    def approxMismatch(self,seq1,seq2,d):
        for c1,c2 in zip(seq1,seq2):
            if c1 != c2:
                if d == 0:
                    return False
                else:
                    d -= 1
        return True
    
if __name__ == "__main__":
    p11 = Problem11()
    print p11.inexactMatches('ACCAC',2,0)
    '''in_file = open("rosalind_1ggggg.txt",'r')
    seq1 = in_file.readline().strip()
    nums = in_file.readline()
    nums = nums.split(" ")
    k = int(nums[0])
    d = int(nums[1])
    out_file = open("prob11_out.txt",'w')
    
    for kmer in p11.freqWordswMismatch(seq1,k,d):
        out_file.write(kmer+" ")
    out_file.flush()'''