# -*- coding: utf-8 -*-
"""
Created on Sun Feb 02 00:46:59 2014

@author: Jeffrey
"""

import time

class Problem21:
    
    def manhattanTourist(self,n,m,down,right):
        lengths = [[0 for x in range(m+1)] for x in range(n+1)]
        for i in range(1,n+1):
            lengths[i][0] = lengths[i-1][0] + down[i-1][0]
        for j in range(1,m+1):
            lengths[0][j] = lengths[0][j-1] + right[0][j-1]
        for i in range(1,n+1):
            for j in range(1,m+1):
                lengths[i][j] = max(lengths[i-1][j]+down[i-1][j],lengths[i][j-1]+right[i][j-1])
        return lengths[i][j]
    



if __name__ == "__main__":
    p21 = Problem21()
    
    start_time = time.time()
    in_file = open("rosalind_5bbb.txt",'r')
    ints = in_file.readline().strip().split(" ")
    n = int(ints[0])
    m = int(ints[1])
    down = []
    line = in_file.readline().strip()
    while line != "-":
        down.append(map(int,line.split(" ")))
        line = in_file.readline().strip()
    
    right = []
    line = in_file.readline().strip()
    while line and line != "":
        right.append(map(int,line.split(" ")))
        line = in_file.readline().strip()
    
    out_file = open("prob21_out.txt",'w')
    
    out = p21.manhattanTourist(n,m,down,right)
    print out
    out_file.write(str(out))
    out_file.flush()
    print time.time() - start_time, "seconds"