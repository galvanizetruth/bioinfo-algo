# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 23:43:10 2014

@author: Jeffrey
"""

import sys,time, bisect

class Problem49:
    
    def makeSuffixArray(self,text):
        suffixes = [('',0) for x in xrange(len(text))]
        for i in xrange(len(text)):
            suffixes[i] = (text[i:],i)
        suffixes.sort()
        lst1, lst2 = zip(*suffixes)
        return lst2
    
    def makeSuffixArray2(self,text):
        suffixes = []
        for i in xrange(len(text)):
            bisect.insort_left(suffixes,(text[i:],i))
        lst1, lst2 = zip(*suffixes)
        return lst2
    
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
    p49 = Problem49()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_7g.txt",'r')
    text = in_file.readline().strip()
    #text2 = 'AACGATAGCGGTAGAGATAGAGAGAGATATACGACTTTTTTTTTTTGAGCTAGCTGGGGGGGGGGATCGATCGTACGATCGATCGGCGCGATCGATGCATGCTATAAAAAAACAGCATCGATCGATCGCATCGATCGATCGATCGATCGATGCATTATATAGTAATATATATATAATATCGTACGTCAGTACTGACTACTGACACTGACTGACTACGCAGTATCGACTGCATGATGTACGACTGATCTACGACTGCAGTATCGACTTACGGCATCGAGTCTGATGCATGCTGATTTAGGGACGATCGATCGATCGATCGTAGCATGCTAGCTAGCCCCCGGGGGGGGGGGGGGGGGGGGGGTTTAGCTAGTCAGTCATGACACGTTGCGATCATCGAGTCCATTCGATACGCAGTTCAGTACGATGCATGCATGCATCGTATCTGCAGACTGTACGTCATAGCTGCAACGTTCGATCGCATGTCGATGCACGTACTGTCAGTACGTACTAGACGTAGCTAGCACTGTGCAATGCTAGCTGCATGACTGACTCAGTACTGCATGCATGACTGCAGTACTGCATGATGCTGAACTGACCAGCTAGCTAGCTGACTGACTGATCGATCGATGCTAGCTAGTCGATCGCGTCGGCAGCTGCGGCGGCGATGCTAGGCGCGGCGACTAGCTAGCTACGTATATATCAATCGACTACGTAGTACGTCGATCGATGCATGCATCGATGCATTAAAAAAAAAACGATCGATCGATGCTAAACGATATAGAGAGATATTTGTCAGTCAGTACGTAGTACATCGATCGATCGATCGGCGCGCGATCGCGCTCTCTCCTATATTATATTTATAGAGAGGGGGACACCCCTACTACTACTATCATCATCTACAGACATCCCAGCCAGA$'
    #text = ''
    #for i in range(11):
    #    text += text2
    
    out_file = open("prob49_out.txt",'w')
    out = p49.makeSuffixArray3(text)

    strout = ""
    for i in out:
        print str(i)+',',
        strout += str(i)+', '
    print
    out_file.write(strout[:-2])
    out_file.flush()
    
    print len(text)

    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"