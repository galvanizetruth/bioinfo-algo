# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 00:34:09 2014

@author: Jeffrey
"""


import time, sys, numpy as np

class Problem32:
    
    def multLCS(self,seq1,seq2,seq3):
        scores = [[[0 for x in range(len(seq3)+1)] for x in range(len(seq2)+1)] for x in range(len(seq1)+1)]
        backtrack = [[[-1 for x in range(len(seq3)+1)] for x in range(len(seq2)+1)] for x in range(len(seq1)+1)]
        
        for i in range(1,len(seq1)+1):
            for j in range(1,len(seq2)+1):
                for k in range(1,len(seq3)+1):
                    match = 0
                    if seq1[i-1] == seq2[j-1] and seq2[j-1] == seq3[k-1]:
                        match = 1
                   
                    values = []
                    values.append(scores[i-1][j-1][k-1]+match)
                    values.append(scores[i-1][j-1][k])
                    values.append(scores[i-1][j][k-1])
                    values.append(scores[i][j-1][k-1])
                    values.append(scores[i-1][j][k])
                    values.append(scores[i][j-1][k])
                    values.append(scores[i][j][k-1])
                    scores[i][j][k] = max(values)
                    backtrack[i][j][k] = argmax(values)
                    
        print backtrack
        i = len(seq1)
        j = len(seq2)
        k = len(seq3)
        out1 = ""
        out2 = ""
        out3 = ""
        while (i != 0 or j != 0 or k != 0) and backtrack[i][j][k] != -1:
            #print backtrack[i][j][k],i,j,k
            if backtrack[i][j][k] == 0:
                out1 = seq1[i-1] + out1
                out2 = seq2[j-1] + out2
                out3 = seq3[k-1] + out3
                #print out1
                #print out2
                #print out3
                i = i-1
                j = j-1
                k = k-1   
            elif backtrack[i][j][k] == 1:
                out1 = seq1[i-1] + out1
                out2 = seq2[j-1] + out2
                out3 = "-" + out3
                i = i-1
                j = j-1
            elif backtrack[i][j][k] == 2:
                out1 = seq1[i-1] + out1
                out2 = "-" + out2
                out3 = seq3[k-1] + out3
                i = i-1
                k = k-1
            elif backtrack[i][j][k] == 3:
                out1 = "-" + out1
                out2 = seq2[j-1] + out2
                out3 = seq3[k-1] + out3
                j = j-1
                k = k-1
            elif backtrack[i][j][k] == 4:
                out1 = seq1[i-1] + out1
                out2 = "-" + out2
                out3 = "-" + out3
                i = i-1
            elif backtrack[i][j][k] == 5:
                out1 = "-" + out1
                out2 = seq2[j-1] + out2
                out3 = "-" + out3
                j = j-1
            elif backtrack[i][j][k] == 6:
                out1 = "-" + out1
                out2 = "-" + out2
                out3 = seq3[k-1] + out3
                k = k-1

        #print i,j,k                     
        if i == 0:
            if j == 0:
                out1 = "-"*k + out1
                out2 = "-"*k + out2
                out3 = seq3[:k] + out3
            elif k == 0:
                out1 = "-"*j + out1
                out2 = seq2[:j] + out2
                out3 = "-"*j + out3
            else:
                if j >= k:
                    out1 = "-"*j + out1
                    out2 = seq2[:j] + out2
                    out3 = "-"*(j-k) + seq3[:k] + out3
                else:
                    out1 = "-"*k + out1
                    out2 = "-"*(k-j) + seq2[:j] + out2
                    out3 = seq3[:k] + out3
        elif j == 0:
            if k == 0:
                out1 = seq1[:i] + out1
                out2 = "-"*i + out2
                out3 = "-"*i + out3
            else:
                if i >= k:
                    out1 = seq1[:i] + out1
                    out2 = "-"*i + out2
                    out3 = "-"*(i-k) + seq3[:k] + out3
                else:
                    out1 = "-"*(k-i) + seq1[:i] + out1
                    out2 = "-"*k + out2
                    out3 = seq3[:k] + out3
        else:
            if i >= j:
                out1 = seq1[:i] + out1
                out2 = "-"*(i-j) + seq2[:j] + out2
                out3 = "-"*i + out3
            else:
                out1 = "-"*(j-i) + seq1[:i] + out1
                out2 = seq2[:j] + out2
                out3 = "-"*j + out3
                

        return (scores[len(seq1)][len(seq2)][len(seq3)],out1,out2,out3)

if __name__ == "__main__":
    p32 = Problem32()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_5mmmm.txt",'r')
    seq1 = in_file.readline().strip()
    seq2 = in_file.readline().strip()
    seq3 = in_file.readline().strip()
    
    out_file = open("prob32_out.txt",'w')
    
    
    (score,align1,align2,align3) = p32.multLCS(seq1,seq2,seq3)
    print score
    print align1
    print align2
    print align3
    out_file.write(str(score)+"\n")
    out_file.write(align1+"\n"+align2+"\n"+align3+"\n")
    out_file.flush()
    
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"