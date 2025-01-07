# -*- coding: utf-8 -*-
"""
Created on Mon Mar 03 00:32:07 2014

@author: Jeffrey
"""

import sys,time

class Problem55:
    
    def makePartialSuffixArray(self,text,k):     
        suff_arr = self.makeSuffixArray3(text)
        out_num = len(suff_arr)/k+1
        out = [(0,0) for x in xrange(out_num)]
        for i in xrange(out_num):
            out[i] = (suff_arr.index(k*i),k*i)
        out.sort()
        return out
    
    def makeSuffixArray3(self,text):
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
        return lst2
                    
if __name__ == "__main__":
    p55 = Problem55()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_7mmm.txt",'r')
    text = in_file.readline().strip()
    k = int(in_file.readline().strip())
    
    out_file = open("prob55_out.txt",'w')
    out = p55.makePartialSuffixArray(text,k)
    for (i,suff_array) in out:
        print str(i)+','+str(suff_array)
        out_file.write(str(i)+','+str(suff_array)+'\n')
    out_file.flush()
    
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"