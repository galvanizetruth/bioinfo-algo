# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 17:46:21 2014

@author: Jeffrey
"""

class FreqWords:
    
    
    def frequentWords(self,text,k):
        #freq_num keeps track of the frequency of the most frequent k-mer
        freq_num = 0
        #most_freq keeps track of the counts of all k-mers
        most_freq = {}
        #mf is a list of the most frequent k-mers for efficiency
        mf = []
        for i in range(len(text)):
            kmer = text[i:i+k]
            if not most_freq.has_key(kmer):
                most_freq[kmer] = 1
            else:
                c = most_freq[kmer] + 1
                most_freq[kmer] = c
                #resets mf
                if c > freq_num:
                    mf = []
                    freq_num = c
                #If c is equal to freq_num, save the kmer
                if c >= freq_num:
                    mf.append(kmer)
        return mf
    
    
if __name__ == "__main__":
    fw = FreqWords()
    in_file = open("rosalind_1a.txt",'r')
    seq = in_file.readline()
    k = int(in_file.readline())
    out_file = open("prob5_out.txt",'w')
    for kmer in fw.frequentWords(seq,k):
        out_file.write(kmer+" ")
    out_file.flush()
    
            