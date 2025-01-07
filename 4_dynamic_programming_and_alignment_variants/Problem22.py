# -*- coding: utf-8 -*-
"""
Created on Sun Feb 02 01:21:26 2014

@author: Jeffrey
"""

import time, sys

class Problem22:
    
    def lcs(self,seq1,seq2):
        scores = [[0 for x in range(len(seq2)+1)] for x in range(len(seq1)+1)]
        backtrack = [[-1 for x in range(len(seq2)+1)] for x in range(len(seq1)+1)]
        for i in range(1,len(seq1)+1):
            backtrack[i][0] = 2
        for j in range(1,len(seq2)+1):
            backtrack[0][j] = 1
        for i in range(1,len(seq1)+1):
            for j in range(1,len(seq2)+1):
                if seq1[i-1] == seq2[j-1]:
                    scores[i][j] = max(scores[i-1][j],scores[i][j-1],scores[i-1][j-1]+1)
                    if scores[i][j] == scores[i-1][j-1]+1:
                        backtrack[i][j] = 0
                    elif scores[i][j] == scores[i][j-1]:
                        backtrack[i][j] = 1
                    elif scores[i][j] == scores[i-1][j]:
                        backtrack[i][j] = 2
                else:
                    scores[i][j] = max(scores[i-1][j],scores[i][j-1],scores[i-1][j-1])
                    if scores[i][j] == scores[i-1][j-1]:
                        backtrack[i][j] = 0
                    elif scores[i][j] == scores[i][j-1]:
                        backtrack[i][j] = 1
                    elif scores[i][j] == scores[i-1][j]:
                        backtrack[i][j] = 2
                
                
                
#                if scores[i-1][j] >= scores[i][j-1] and scores[i-1][j] >= scores[i-1][j-1]+match:
#                    scores[i][j] = scores[i-1][j]
#                    backtrack[i][j] = 2
#                elif scores[i][j-1] >= scores[i-1][j] and scores[i][j-1] >= scores[i-1][j-1]+match:
#                    scores[i][j] = scores[i][j-1]
#                    backtrack[i][j] = 1
#                elif scores[i-1][j-1]+match >= scores[i-1][j] and scores[i-1][j-1]+match >= scores[i][j-1]:
#                    scores[i][j] = scores[i-1][j-1]+match
#                    backtrack[i][j] = 0
        for x in range(len(scores)):
            print scores[x]
        print ""
        for x in range(len(backtrack)):
            print backtrack[x]

        return self.outputLCS(backtrack,seq1,len(seq1),len(seq2))
    
    def outputLCS(self,backtrack,v,i,j):
        if i == 0 and j == 0:
            return ""
        if backtrack[i][j] == 0:
            return self.outputLCS(backtrack,v,i-1,j-1) + v[i-1]        
        elif backtrack[i][j] == 1:
            return self.outputLCS(backtrack,v,i,j-1)
        elif backtrack[i][j] == 2:
            return self.outputLCS(backtrack,v,i-1,j)
        

if __name__ == "__main__":
    p22 = Problem22()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    in_file = open("rosalind_5cc.txt",'r')
    seq1 = in_file.readline().strip()
    seq2 = in_file.readline().strip()
    
    out_file = open("prob22_out.txt",'w')
    
    out = p22.lcs(seq1,seq2)
    print out
    out_file.write(str(out))
    out_file.flush()
    print time.time() - start_time, "seconds"