# -*- coding: utf-8 -*-
"""
Created on Mon Feb 03 02:54:07 2014

@author: Jeffrey
"""

import time, sys

class Problem25:
    
    def localAlignment(self,aa_dict,pam,gap,seq1,seq2):
        scores = [[0 for x in range(len(seq2)+1)] for x in range(len(seq1)+1)]
        backtrack = [[-1 for x in range(len(seq2)+1)] for x in range(len(seq1)+1)]
        for i in range(1,len(seq1)+1):
            scores[i][0] = scores[i-1][0] - gap
        for j in range(1,len(seq2)+1):
            scores[0][j] = scores[0][j-1] - gap
        for i in range(1,len(seq1)+1):
            for j in range(1,len(seq2)+1):
                match = pam[aa_dict[seq1[i-1]]][aa_dict[seq2[j-1]]]
                scores[i][j] = max(scores[i-1][j]-gap,scores[i][j-1]-gap,scores[i-1][j-1]+match,0)

                if scores[i][j] == scores[i-1][j]-gap:
                    backtrack[i][j] = 2
                elif scores[i][j] == scores[i][j-1]-gap:
                    backtrack[i][j] = 1
                elif scores[i][j] == scores[i-1][j-1]+match:
                    backtrack[i][j] = 0
                elif scores[i][j] == 0:
                    backtrack[i][j] = -1

        maxI = len(seq1)
        maxJ = len(seq2)
        maxScore = 0
        for i in range(len(seq1)+1):
            for j in range(len(seq2)+1):
                if scores[i][j] > maxScore:
                    maxScore = scores[i][j]
                    maxI = i
                    maxJ = j

        i = maxI
        j = maxJ
        out1 = ""
        out2 = ""
        while i != 0 and j != 0 and backtrack[i][j] != -1:
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

        return (scores[maxI][maxJ],out1,out2)
    

if __name__ == "__main__":
    p25 = Problem25()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    pamfile = open("pam250.txt",'r')
    aa = pamfile.readline().strip().split("  ")
    aa_dict = {}
    for i in range(len(aa)):
        aa_dict[aa[i]] = i
    
    pam_matrix = [[-50 for x in range(len(aa_dict))] for x in range(len(aa_dict))]
    line = pamfile.readline().strip()
    while line and line != "":
        i = 0
        currAA = ''
        for x in line.split(" "):
            if aa_dict.has_key(x):
                currAA = x
            elif x != '':
                pam_matrix[aa_dict[currAA]][i] = int(x)
                i += 1
        line = pamfile.readline().strip()

    gap_score = 5
    in_file = open("rosalind_5f.txt",'r')
    seq1 = in_file.readline().strip()
    seq2 = in_file.readline().strip()
    
    out_file = open("prob25_out.txt",'w')
    
    
    (score,align1,align2) = p25.localAlignment(aa_dict,pam_matrix,gap_score,seq1,seq2)
    print score
    print align1
    print align2
    out_file.write(str(score)+"\n")
    out_file.write(align1+"\n"+align2)
    out_file.flush()
    print time.time() - start_time, "seconds"