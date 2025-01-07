# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 12:42:37 2014

@author: Jeffrey
"""

class CSE282_Prob4:
    
    def sharedKMers(self, k, g1, g2):
        '''Input: a number, k, and two gene sequences, g1 and g2
        Output: the ordered pairs of the starting indices of the k-mers
        that are shared between g1 and g2, including identical k-mers
        and reverse complementary k-mers.'''
        
        in_file = open("rosalind_6d.txt","r")
        k = int(in_file.readline())
        g1 = in_file.readline()
        g2 = in_file.readline()
        
        #Make dictionary of all of the k-mers of g1
        #Contains a list because the same k-mer can appear multiple times
        kmer_list = {}
        for i in range(len(g1)-k+1):
            if(not kmer_list.has_key(g1[i:i+k])):
                kmer_list[g1[i:i+k]] = [i]
            else:
                kmer_list[g1[i:i+k]].append(i)
        #Check whether any of the k-mers of g2 match the k-mers in kmer_list
        out_list = []
        for i in range(len(g2)-k+1):
            if(kmer_list.has_key(g2[i:i+k])):
                for index in kmer_list[g2[i:i+k]]:
                    out_list.append((index,i))
            #Checks reverse complements but doesn't count palindromes twice
            elif(kmer_list.has_key(self.revComp(g2[i:i+k]))):
                for index in kmer_list[self.revComp(g2[i:i+k])]:
                    out_list.append((index,i))
        
        out_file = open("prob4_out.txt",'w')
        for pair in out_list:
            out_file.write(str(pair)+'\n')
        
        out_file.flush()
        
    def revComp(self, seq):
        '''Input: a gene sequence, seq, of A's, C's, G's and T's
        Output: the reverse complementary sequence of seq'''
        
        out = ''
        for b in seq:
            if b == 'A':
                out += 'T'
            elif b == 'T':
                out += 'A'
            elif b == 'C':
                out += 'G'
            elif b == 'G':
                out += 'C'
            else:
                out += 'N'
        return out[::-1]
        
if __name__ == "__main__":
    p4 = CSE282_Prob4()
    p4.sharedKMers(3,"AAACTCATCAAA","TTTCAAATC")
