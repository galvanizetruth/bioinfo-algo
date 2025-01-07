# -*- coding: utf-8 -*-
"""
Created on Sun Mar 02 05:08:11 2014

@author: Jeffrey
"""


import sys,time

class Problem52:
    
    def inverse_bwt(self,text):
        print(text)
        order = {}
        for i in range(len(text)):
            if not order.has_key(text[i]):
                order[text[i]] = [i]
            else:
                order[text[i]].append(i)
        f_list = list(text)
        f_list.sort()
        first = ''.join(f_list)
        print first
        print order
        countBase = {}
        baseNumber = [0 for x in range(len(first))]
        for i in range(len(first)):
            if not countBase.has_key(first[i]):
                countBase[first[i]] = 1
                baseNumber[i] = 1
            else:
                countBase[first[i]] += 1
                baseNumber[i] = countBase[first[i]]
        print countBase
        print baseNumber
        currIndex = 0
        currBase = first[0]
        currNumber = 1
        out = currBase
        for i in range(len(text)-1):
            currIndex = order[currBase][currNumber-1]
            currNumber = baseNumber[currIndex]
            currBase = first[currIndex]
            out += currBase
        out = out[1:]+out[0]
        return out
        
if __name__ == "__main__":
    p52 = Problem52()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_7jtest.txt",'r')
    text = in_file.readline().strip()
    
    out_file = open("prob52_out.txt",'w')
    out = p52.inverse_bwt(text)

    print out
    out_file.write(out+'\n')
    out_file.flush()
    
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"