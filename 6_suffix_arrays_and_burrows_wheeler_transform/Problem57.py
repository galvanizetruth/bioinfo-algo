# -*- coding: utf-8 -*-
"""
Created on Mon Mar 03 14:40:09 2014

@author: Jeffrey
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 03 10:51:50 2014

@author: Jeffrey
"""

import sys,time

class Problem57:
    
    def multipleApproxPatternMatch(self,old_text,patterns,d):
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
            currIndices = {}
            currD = d
            while currD >= 0:
                currBase = patterns[i][d-currD]
                #print currBase
                for index in order[currBase]:
                    #print order[currBase]
                    hasPattern = True
                    currIndex = index
                    currNumber = 0
                    numMismatches = currD
                    for j in range(1,len(patterns[i])):
                        currBase = first[currIndex]
                        #print currBase, patterns[i][j], index, f_order[index], numMismatches
                        if currBase != patterns[i][j]:
                            numMismatches -= 1
                            if numMismatches < 0:
                                hasPattern = False
                                break
                        currNumber = baseNumber[currIndex]
                        currIndex = order[currBase][currNumber-1]
                    if hasPattern:
                        key = suff_arr[f_order[index]]
                        if not currIndices.has_key(key):
                            indices.append(suff_arr[f_order[index]])
                            currIndices[key] = 1
                currD -= 1
                if(len(patterns[i])-1 < d-currD):
                    break
        indices.sort()
        return indices

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
    p57 = Problem57()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_7ostepic.txt",'r')
    text = in_file.readline().strip()+'$'

    patterns = []
    line = in_file.readline().strip()
    while line and line != "":
        patterns.append(line)
        line = in_file.readline().strip()
    d = int(patterns.pop())
    patterns = patterns[0].split(' ')
    
    out_file = open("prob57_out.txt",'w')
    
    out = p57.multipleApproxPatternMatch(text,patterns,d)
    for i in out:
        print str(i),
        out_file.write(str(i)+' ')
    print
    out_file.flush()
    
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"