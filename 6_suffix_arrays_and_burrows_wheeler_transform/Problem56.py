# -*- coding: utf-8 -*-
"""
Created on Mon Mar 03 10:51:50 2014

@author: Jeffrey
"""

import sys,time

class Problem56:
    
    def multiplePatternMatch(self,old_text,patterns):
        (text,suff_arr) = self.makeSuffixArrayAndBWT(old_text)
        #print 'str',old_text
        #print 'bwt',text
        #print 'sa',suff_arr
        order = {}
        for i in range(len(text)):
            if not order.has_key(text[i]):
                order[text[i]] = [i]
            else:
                order[text[i]].append(i)
        f_list = list(text)
        f_list.sort()
        first = ''.join(f_list)
        #print 'first',first
        countBase = {}
        baseNumber = [0 for x in range(len(first))]
        f_order = [0 for x in range(len(first))]
        for i in range(len(first)):
            if not countBase.has_key(first[i]):
                countBase[first[i]] = 1
                baseNumber[i] = 1
            else:
                countBase[first[i]] += 1
                baseNumber[i] = countBase[first[i]]
            #print order[first[i]],baseNumber[i],i,first[i]
            f_order[order[first[i]][baseNumber[i]-1]] = i
        
        #print 'forder',f_order
            
        indices = []
        #print patterns
        for i in range(len(patterns)):
            currBase = patterns[i][0]
            for index in order[currBase]:
                #print order[currBase]
                hasPattern = True
                currIndex = index
                currNumber = 0
                for j in range(1,len(patterns[i])):
                    currBase = first[currIndex]
                    #print currBase, patterns[i][j], index, f_order[index]
                    if currBase != patterns[i][j]:
                        hasPattern = False
                        break
                    currNumber = baseNumber[currIndex]
                    currIndex = order[currBase][currNumber-1]
                if hasPattern:
                    indices.append(suff_arr[f_order[index]])
        indices.sort()
        return indices
    
    def makePartialSuffixArray(self,text,k):     
        suff_arr = self.makeSuffixArray3(text)
        out_num = len(suff_arr)/k+1
        out = [(0,0) for x in xrange(out_num)]
        for i in xrange(out_num):
            out[i] = (suff_arr.index(k*i),k*i)
        out.sort()
        return out
    
    def makeSuffixArrayAndBWT(self,text):
        k = 1
        k_dict = {}
        textlen = len(text)
        while (k < textlen):
            noRepeats = True
            k_dict = {}
            for i in xrange(textlen):
                kmer = text[i:i+k]
                if k_dict.has_key(kmer):
                    noRepeats = False
                    break
                k_dict[kmer] = (kmer,i)
            if noRepeats:
                break
            k += 1
        
        unique = k_dict.values()[:]
        unique.sort()
        lst1, lst2 = zip(*unique)
        bwt = ""
        for i in list(lst2):
            bwt += text[i-1]

        return (bwt,lst2)
                    
if __name__ == "__main__":
    p56 = Problem56()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_7n.txt",'r')
    text = in_file.readline().strip()+'$'

    patterns = []
    line = in_file.readline().strip()
    while line and line != "":
        patterns.append(line)
        line = in_file.readline().strip()
    
    out_file = open("prob56_out.txt",'w')
    
    out = p56.multiplePatternMatch(text,patterns)
    for i in out:
        print str(i),
        out_file.write(str(i)+' ')
    print
    out_file.flush()
    
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"