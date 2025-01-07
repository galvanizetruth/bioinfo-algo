# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:03:18 2014

@author: Jeffrey
"""

class Problem8:
    
    def count(self,text,pattern,k):
        count = 0
        for i in range(len(text)+k-1):
            if text[i:i+k] == pattern:
                count += 1
        return count
        
    
    def clumpFinder(self,genome,k,l,t):
        '''Given a genome, look in windows of length l, and find all k-mers
        that appear at least t times in some window in genome'''
        output = []
        #Iterate through windows of length l over genome
        for i in range(len(genome)-l+1):
            window = genome[i:i+l]
            #There is a new kmer list for each window
            kmer_list = {}
            for j in range(len(window)+k-1):
                #Keep counts of each kmer that appears in the window
                kmer = window[j:j+k]
                if not kmer_list.has_key(kmer):
                    kmer_list[kmer] = 1
                else:
                    kmer_list[kmer] += 1
                    #Append if count is >= t
                    if kmer_list[kmer] >= t and kmer not in output:
                        output.append(kmer)
        return output
        
if __name__ == "__main__":
    p8 = Problem8()
    
    in_file = open("rosalind_1d.txt",'r')
    seq1 = in_file.readline()
    nums = in_file.readline()
    seq1 = seq1[:len(seq1)-1]
    nums = nums.split(" ")
    k = int(nums[0])
    l = int(nums[1])
    t = int(nums[2])
    out_file = open("prob8_out.txt",'w')
    
    for kmer in p8.clumpFinder(seq1,k,l,t):
        out_file.write(kmer+" ")
    out_file.flush()