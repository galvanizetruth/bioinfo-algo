# -*- coding: utf-8 -*-
"""
Created on Sun Mar 02 04:48:46 2014

@author: Jeffrey
"""


import sys,time

class Problem51:
    
    def bwt(self,text):
        mat = ['' for i in range(len(text))]
        curr = text
        for i in range(len(text)):
            curr = curr[-1]+curr[:-1]
            mat[i] = curr
        mat.sort()
        out = ''
        for i in range(len(text)):
            out += mat[i][-1]
        return out
    
    def countRepeats(self,text):
        currB = "D"
        count = 0
        for i in range(len(text)):
            if text[i] == currB:
                count += 1
            else:
                currB = text[i]
        return count
        
if __name__ == "__main__":
    p51 = Problem51()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_7i.txt",'r')
    text = in_file.readline().strip()
    #text = "GCTGAGCATC$"
    
    out_file = open("prob51_out.txt",'w')
    out = p51.bwt(text)
    
    print out
    
    print
    print p51.countRepeats(text)
    print p51.countRepeats(out)
    out_file.write(out+'\n')
    out_file.flush()
    
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"