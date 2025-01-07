# -*- coding: utf-8 -*-
"""
Created on Thu Feb 06 02:50:11 2014

@author: Jeffrey
"""

import time, sys
import numpy as np

class Problem29:
    
    def affineGapAlignment(self,aa_dict,blos,gap_open,gap_extend,seq1,seq2):
        match = [[0 for x in range(len(seq2)+1)] for x in range(len(seq1)+1)]
        down = [[0 for x in range(len(seq2)+1)] for x in range(len(seq1)+1)]
        right = [[0 for x in range(len(seq2)+1)] for x in range(len(seq1)+1)]
        best = [[0 for x in range(len(seq2)+1)] for x in range(len(seq1)+1)]
        backtrack = [[-1 for x in range(len(seq2)+1)] for x in range(len(seq1)+1)]
        for i in range(1,len(seq1)+1):
            match[i][0] = -np.inf
            down[i][0] = gap_open+i*gap_extend
            right[i][0] = -np.inf
            best[i][0] = max(match[i][0],down[i][0],right[i][0])
        for j in range(1,len(seq2)+1):
            match[0][j] = -np.inf
            down[0][j] = -np.inf
            right[0][j] = gap_open+j*gap_extend
            best[0][j] = max(match[0][j],down[0][j],right[0][j])
        for i in range(1,len(seq1)+1):
            for j in range(1,len(seq2)+1):
                m = blos[aa_dict[seq1[i-1]]][aa_dict[seq2[j-1]]]
                match[i][j] = m+max(match[i-1][j-1],down[i-1][j-1],right[i-1][j-1])
                down[i][j] = max(match[i-1][j]+gap_open,down[i-1][j]+gap_extend)#,right[i-1][j]+gap_open)
                right[i][j] = max(match[i][j-1]+gap_open,right[i][j-1]+gap_extend)#,down[i][j-1]+gap_open)
                
                bestScore = max(match[i][j],down[i][j],right[i][j])
                best[i][j] = bestScore
                
                if bestScore == down[i][j]:
                    backtrack[i][j] = 2
                elif bestScore == right[i][j]:
                    backtrack[i][j] = 1
                elif bestScore == match[i][j]:
                    backtrack[i][j] = 0

        print np.array(match)
        print np.array(down)
        print np.array(right)
        print np.array(best)
        
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
        return (max(match[len(seq1)][len(seq2)],down[len(seq1)][len(seq2)],right[len(seq1)][len(seq2)]),out1,out2)
    

if __name__ == "__main__":
    p29 = Problem29()
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
        
    gap_open = -11
    gap_extend = -1
    in_file = open("rosalind_5jj.txt",'r')
    seq1 = in_file.readline().strip()
    seq2 = in_file.readline().strip()
    #seq1 = 'YHFDVPDCWAHRYWVENPQAIAQMEQICFNWFPSMMMKQPHVFKVDHHMSCRWLPIRGKKCSSCCTRMRVRTVWE'
    #seq2 = 'YHEDVAHEDAIAQMVNTFGFVWQICLNQFPSMMMKIYWIAVLSAHVADRKTWSKHMSCRWLPIISATCARMRVRTVWE'
    
    out_file = open("prob29_out.txt",'w')
    
    
    (score,align1,align2) = p29.affineGapAlignment(aa_dict,blosum_matrix,gap_open,gap_extend,seq1,seq2)
    print score
    print align1
    print align2
    out_file.write(str(score)+"\n")
    out_file.write(align1+"\n"+align2)
    out_file.flush()
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"