# -*- coding: utf-8 -*-
"""
Created on Mon Feb 03 02:02:23 2014

@author: Jeffrey
"""

import time, sys, numpy as np

class Problem24:
    
    def globalAlignment(self,aa_dict,blos,gap,seq1,seq2):
        scores = [[0 for x in range(len(seq2)+1)] for x in range(len(seq1)+1)]
        backtrack = [[-1 for x in range(len(seq2)+1)] for x in range(len(seq1)+1)]
        for i in range(1,len(seq1)+1):
            scores[i][0] = scores[i-1][0] - gap
        for j in range(1,len(seq2)+1):
            scores[0][j] = scores[0][j-1] - gap
        for i in range(1,len(seq1)+1):
            for j in range(1,len(seq2)+1):
                match = blos[aa_dict[seq1[i-1]]][aa_dict[seq2[j-1]]]
                scores[i][j] = max(scores[i-1][j]-gap,scores[i][j-1]-gap,scores[i-1][j-1]+match)

                if scores[i][j] == scores[i-1][j]-gap:
                    backtrack[i][j] = 2
                elif scores[i][j] == scores[i][j-1]-gap:
                    backtrack[i][j] = 1
                elif scores[i][j] == scores[i-1][j-1]+match:
                    backtrack[i][j] = 0

        i = len(seq1)
        j = len(seq2)
        out1 = ""
        out2 = ""
        while i != 0 and j != 0:
            if backtrack[i][j] == 2:                
                out1 = seq1[i-1] + out1
                out2 = "-" + out2
                i = i-1
            elif backtrack[i][j] == 1:
                out1 = "-" + out1
                out2 = seq2[j-1] + out2
                j = j-1
            else:
                out1 = seq1[i-1] + out1
                out2 = seq2[j-1] + out2
                i = i-1
                j = j-1
        if i == 0:
            out1 = "-"*j + out1
            out2 = seq2[:j] + out2
        elif j == 0:
            out1 = seq1[:i] + out1
            out2 = "-"*i + out2
        return (scores[len(seq1)][len(seq2)],out1,out2)
    

if __name__ == "__main__":
    p24 = Problem24()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    blosumfile = open("blosum.txt",'r')
    aa = blosumfile.readline().strip().split("  ")
    aa_dict = {}
    for i in range(len(aa)):
        aa_dict[aa[i]] = i
    
    blosum_matrix = [[-50 for x in range(len(aa_dict))] for x in range(len(aa_dict))]
    line = blosumfile.readline().strip()
    while line and line != "":
        i = 0
        currAA = ''
        for x in line.split(" "):
            if aa_dict.has_key(x):
                currAA = x
            elif x != '':
                blosum_matrix[aa_dict[currAA]][i] = int(x)
                i += 1
        line = blosumfile.readline().strip()
        
    gap_score = -1
    in_file = open("rosalind_5l.txt",'r')
    seq1 = in_file.readline().strip()
    seq2 = in_file.readline().strip()
    print np.array(blosum_matrix)
    seq1 = "AGC"
    seq2 = "T"
    
    out_file = open("prob24_out.txt",'w')
    
    
    (score,align1,align2) = p24.globalAlignment(aa_dict,blosum_matrix,gap_score,seq1,seq2)
    print score
    print align1
    print align2
    out_file.write(str(score)+"\n")
    out_file.write(align1+"\n"+align2)
    out_file.flush()
    print time.time() - start_time, "seconds"