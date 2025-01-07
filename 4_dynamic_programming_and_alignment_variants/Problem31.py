# -*- coding: utf-8 -*-
"""
Created on Fri Feb 07 13:58:03 2014

@author: Jeffrey
"""


import time, sys

class Problem31:
    
    def globalAlignmentLinSpace(self,aa_dict,blos,gap,seq1,seq2):
        (a1,a2) = self.align(aa_dict,blos,gap,seq1,seq2)
        
        jPrefix = self.forwardPrefixes(aa_dict,blos,gap,seq1,seq2,len(seq2)/2)
        jSuffix = self.reverseSuffixes(aa_dict,blos,gap,seq1,seq2,len(seq2)/2)
        sumScores = [x + y for (x,y) in zip(jPrefix,jSuffix)]
        score = max(sumScores)

        return(score,a1,a2)
        
    def align(self,aa_dict,blos,gap,seq1,seq2):
        m = len(seq1)
        n = len(seq2)
        out1 = ""
        out2 = ""
        if m == 0 or n == 0:
            if m == 0:
                out1 += '-'*n
                out2 = seq2
            elif n==0:
                out1 = seq1
                out2 += '-'*m
        elif m == 1 or n == 1:
            if m == 1:
                (align1,align2) = self.globalAlignment(aa_dict,blos,gap,seq1,seq2)
            elif n == 1:
                (align2,align1) = self.globalAlignment(aa_dict,blos,gap,seq2,seq1)
            out1 = align1
            out2 = align2
            #print seq1,seq2,align1,align2
        else:
            jPrefix = self.forwardPrefixes(aa_dict,blos,gap,seq1,seq2,n/2)
            jSuffix = self.reverseSuffixes(aa_dict,blos,gap,seq1,seq2,n/2)
            #print jPrefix
            #print jSuffix
            
            sumScores = [x + y for (x,y) in zip(jPrefix,jSuffix)]
            maxSum = -1*10**10
            maxI = -1
            for i in range(len(sumScores)):
                if maxSum < sumScores[i]:
                    maxSum = sumScores[i]
                    maxI = i
            #maxScore = max(sumScores)
            #maxI = argmax(sumScores)
            
        
            #print seq1,seq2, maxI, maxScore
            (a1,a2) = self.align(aa_dict,blos,gap,seq1[0:maxI],seq2[0:n/2])
            (a3,a4) = self.align(aa_dict,blos,gap,seq1[maxI:m],seq2[n/2:n])
            out1 = a1+a3
            out2 = a2+a4
        return (out1,out2)
    
    def midEdgeLinSpace(self,aa_dict,blos,gap,seq1,seq2):
        scoresF = [0 for x in range(len(seq1)+1)]
        mid = len(seq2)/2
        for i in range(1,len(seq1)+1):
            scoresF[i] = scoresF[i-1] + gap
        for j in range(1,mid+1):
            currScore = 0
            prevScore = j*gap
            for i in range(1,len(seq1)+1):
                match = blos[aa_dict[seq1[i-1]]][aa_dict[seq2[j-1]]]
                currScore = max(prevScore+gap,scoresF[i]+gap,scoresF[i-1]+match)
                scoresF[i-1] = prevScore
                prevScore = currScore
            scoresF[len(seq1)] = currScore
        
        scoresR = [0 for x in range(len(seq1)+1)]
        for i in range(0,len(seq1))[::-1]:
            scoresR[i] = scoresR[i+1] + gap
        for j in range(mid,len(seq2))[::-1]:
            currScore = 0
            prevScore = (len(seq2)-j)*gap
            for i in range(0,len(seq1))[::-1]:
                match = blos[aa_dict[seq1[i]]][aa_dict[seq2[j]]]
                currScore = max(prevScore+gap,scoresR[i]+gap,scoresR[i+1]+match)
                scoresR[i+1] = prevScore
                prevScore = currScore
            
            scoresR[0] = currScore
            
        sumScores = [x + y for (x,y) in zip(scoresF,scoresR)]
        maxScore = max(sumScores)
        maxI = argmax(sumScores)
        
        return (maxI,mid)
        
    def forwardPrefixes(self,aa_dict,blos,gap,seq1,seq2,index):
        scoresF = [0 for x in range(len(seq1)+1)]
        mid = index
        for i in range(1,len(seq1)+1):
            scoresF[i] = scoresF[i-1] + gap
        for j in range(1,mid+1):
            currScore = 0
            prevScore = j*gap
            for i in range(1,len(seq1)+1):
                match = blos[aa_dict[seq1[i-1]]][aa_dict[seq2[j-1]]]
                currScore = max(prevScore+gap,scoresF[i]+gap,scoresF[i-1]+match)
                scoresF[i-1] = prevScore
                prevScore = currScore
            scoresF[len(seq1)] = currScore
        
        return scoresF
    
    def reverseSuffixes(self,aa_dict,blos,gap,seq1,seq2,index):
        scoresR = [0 for x in range(len(seq1)+1)]
        mid = index
        for i in range(0,len(seq1))[::-1]:
            scoresR[i] = scoresR[i+1] + gap
        for j in range(mid,len(seq2))[::-1]:
            currScore = 0
            prevScore = (len(seq2)-j)*gap
            for i in range(0,len(seq1))[::-1]:
                match = blos[aa_dict[seq1[i]]][aa_dict[seq2[j]]]
                currScore = max(prevScore+gap,scoresR[i]+gap,scoresR[i+1]+match)
                scoresR[i+1] = prevScore
                prevScore = currScore
            
            scoresR[0] = currScore
        
        return scoresR
        
    def globalAlignment(self,aa_dict,blos,gap,string1,seq2):
        maxJ = 0
        maxScore = gap
        for j in range(len(seq2)):
            score = blos[aa_dict[string1[0]]][aa_dict[seq2[j]]]
            if score > maxScore:
                maxScore = score
                maxJ = j
        #print maxJ, maxScore, gap
        if gap > maxScore:
            out1 = string1+'-'*len(seq2)
            out2 = '-'+seq2
        else:
            out1 = '-'*(maxJ)+string1+'-'*(len(seq2)-maxJ-1)
            out2 = seq2
        #print string1,seq2,out1,out2
        return (out1,out2)
    
    def globalAlignment2(self,aa_dict,blos,gap,seq1,seq2):
        scores = [[0 for x in range(len(seq2)+1)] for x in range(len(seq1)+1)]
        backtrack = [[-1 for x in range(len(seq2)+1)] for x in range(len(seq1)+1)]
        for i in range(1,len(seq1)+1):
            scores[i][0] = scores[i-1][0] + gap
        for j in range(1,len(seq2)+1):
            scores[0][j] = scores[0][j-1] + gap
        for i in range(1,len(seq1)+1):
            for j in range(1,len(seq2)+1):
                match = blos[aa_dict[seq1[i-1]]][aa_dict[seq2[j-1]]]
                scores[i][j] = max(scores[i-1][j]+gap,scores[i][j-1]+gap,scores[i-1][j-1]+match)

                if scores[i][j] == scores[i-1][j]+gap:
                    backtrack[i][j] = 2
                elif scores[i][j] == scores[i][j-1]+gap:
                    backtrack[i][j] = 1
                elif scores[i][j] == scores[i-1][j-1]+match:
                    backtrack[i][j] = 0
                    
        i = len(seq1)
        j = len(seq2)
        out1 = ""
        out2 = ""
        while i != 0 and j != 0:
            #print j,i
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
    p31 = Problem31()
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
        
    gap = -5
    in_file = open("rosalind_5l2.txt",'r')
    seq1 = in_file.readline().strip()
    seq2 = in_file.readline().strip()
    
    out_file = open("prob31_out.txt",'w')
    
    
    (score,align1,align2) = p31.globalAlignmentLinSpace(aa_dict,blosum_matrix,gap,seq1,seq2)
    #p31.globalAlignment(aa_dict,blosum_matrix,-1*gap,seq1,seq2)
    print score
    print align1
    print align2
    out_file.write(str(score)+"\n")
    out_file.write(align1+"\n"+align2)
    out_file.flush()
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"