# -*- coding: utf-8 -*-
"""
Created on Thu Feb 06 02:29:42 2014

@author: Jeffrey
"""


import time, sys

class Problem28:
    
    def overlapAlignment(self,seq1,seq2):
        gap = 2
        scores = [[0 for x in range(len(seq2)+1)] for x in range(len(seq1)+1)]
        backtrack = [[-1 for x in range(len(seq2)+1)] for x in range(len(seq1)+1)]

        for j in range(1,len(seq2)+1):
            scores[0][j] = scores[0][j-1] - gap
        for i in range(1,len(seq1)+1):
            for j in range(1,len(seq2)+1):
                match = -2
                if seq1[i-1] == seq2[j-1]:
                    match = 1
                scores[i][j] = max(scores[i-1][j]-gap,scores[i][j-1]-gap,scores[i-1][j-1]+match)

                if scores[i][j] == scores[i-1][j-1]+match:
                    backtrack[i][j] = 0
                elif scores[i][j] == scores[i-1][j]-gap:
                    backtrack[i][j] = 2
                elif scores[i][j] == scores[i][j-1]-gap:
                    backtrack[i][j] = 1
                

        maxJ = len(seq2)
        maxScore = 0
        for j in range(len(seq2)+1):
            if scores[len(seq1)][j] > maxScore:
                maxScore = scores[len(seq1)][j]
                maxJ = j

        i = len(seq1)
        j = maxJ
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


        return (scores[len(seq1)][maxJ],out1,out2)
    
    

if __name__ == "__main__":
    p28 = Problem28()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_5iii.txt",'r')
    seq1 = in_file.readline().strip()
    seq2 = in_file.readline().strip()
    
    out_file = open("prob28_out.txt",'w')
    
    
    (score,align1,align2) = p28.overlapAlignment(seq1,seq2)
    print score
    print align1
    print align2
    out_file.write(str(score)+"\n")
    out_file.write(align1+"\n"+align2+"\n")
    out_file.flush()
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"