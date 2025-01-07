# -*- coding: utf-8 -*-
"""
Created on Sun Mar 02 22:27:17 2014

@author: Jeffrey
"""

import sys,time

class Problem53:
    
    def bwMatching(self,text,patterns):
        order = {}
        for i in range(len(text)):
            if not order.has_key(text[i]):
                order[text[i]] = [i]
            else:
                order[text[i]].append(i)
        f_list = list(text)
        f_list.sort()
        first = ''.join(f_list)
        countBase = {}
        baseNumber = [0 for x in range(len(first))]
        for i in range(len(first)):
            if not countBase.has_key(first[i]):
                countBase[first[i]] = 1
                baseNumber[i] = 1
            else:
                countBase[first[i]] += 1
                baseNumber[i] = countBase[first[i]]
        
        counts = [0 for x in range(len(patterns))]
        for i in range(len(patterns)):
            currBase = patterns[i][0]
            for index in order[currBase]:
                hasPattern = True
                currIndex = index
                currNumber = 0
                for j in range(1,len(patterns[i])):
                    currBase = first[currIndex]
                    if currBase != patterns[i][j]:
                        hasPattern = False
                        break
                    currNumber = baseNumber[currIndex]
                    currIndex = order[currBase][currNumber-1]
                if hasPattern:
                    counts[i] += 1
        
        return counts
                    
if __name__ == "__main__":
    p53 = Problem53()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_7k.txt",'r')
    text = in_file.readline().strip()
    pattern_str = in_file.readline().strip()
    patterns = pattern_str.split(" ")
    
    out_file = open("prob53_out.txt",'w')
    out = p53.bwMatching(text,patterns)

    for i in out:
        print i,
        out_file.write(str(i)+' ')
    out_file.flush()
    
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"