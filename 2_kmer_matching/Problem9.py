# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:37:33 2014

@author: Jeffrey
"""

class Problem9:
    
    def minimumSkew(self, genome):
        '''Given a sequence, genome, find the skew from all prefixes of
        the genome: ['','A','AC'] where skew is numG's - numC's, and 
        return indices where the skew of the prefix is minimized'''
        skew_list = []
        minimum = 0
        index_list = []
        for i in range(-1,len(genome)):
            if i == -1:
                skew_list.append(0)
            else:
                #The next skew is either -1, +1, or = the previous skew
                if genome[i] == "C":
                    skew_list.append(skew_list[i] + -1)
                elif genome[i] == "G":
                    skew_list.append(skew_list[i] + 1)
                else:
                    skew_list.append(skew_list[i])
                #Compare newly appended skew to minimum
                if skew_list[i+1] < minimum:
                    index_list = []
                    minimum = skew_list[i+1]
                    index_list.append(i+1)
                elif skew_list[i+1] == minimum:
                    index_list.append(i+1)
        return index_list
        
if __name__ == "__main__":
    p9 = Problem9()
    
    in_file = open("rosalind_1e.txt",'r')
    seq1 = in_file.readline()
    seq1 = seq1[:len(seq1)]
    out_file = open("prob9_out.txt",'w')
    
    for index in p9.minimumSkew(seq1):
        out_file.write(str(index)+" ")
    out_file.flush()