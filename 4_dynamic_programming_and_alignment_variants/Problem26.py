# -*- coding: utf-8 -*-
"""
Created on Thu Feb 06 00:29:18 2014

@author: Jeffrey
"""

import time, sys

class Problem26:
    
    def editDistance(self,seq1,seq2):
        gap = -1
        scores = [[0 for x in range(len(seq2)+1)] for x in range(len(seq1)+1)]
        for i in range(1,len(seq1)+1):
            scores[i][0] = scores[i-1][0] - gap
        for j in range(1,len(seq2)+1):
            scores[0][j] = scores[0][j-1] - gap
        for i in range(1,len(seq1)+1):
            for j in range(1,len(seq2)+1):
                match = 1
                if seq1[i-1] == seq2[j-1]:
                    match = 0
                scores[i][j] = min(scores[i-1][j]-gap,scores[i][j-1]-gap,scores[i-1][j-1]+match)

        return scores[len(seq1)][len(seq2)]
    
    

if __name__ == "__main__":
    p26 = Problem26()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    gap_score = 1
    in_file = open("rosalind_5ggg.txt",'r')
    seq1 = in_file.readline().strip()
    seq2 = in_file.readline().strip()
    
    out_file = open("prob26_out.txt",'w')
    
    
    score = p26.editDistance(seq1,seq2)
    print score
    out_file.write(str(score))
    out_file.flush()
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"