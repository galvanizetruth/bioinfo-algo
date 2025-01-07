# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 12:56:17 2014

@author: Jeffrey
"""


import time, sys

class Problem42:
    
    def contigGeneration(self,kmers):
        graph = self.deBruijnKmer(kmers)
        contigs = []
        (ins,outs) = self.findBalance(graph)
        while graph:
            start_key = graph.keys()[0]
            contig = []
            key = start_key
            while graph and graph.has_key(key):
                contig.append(key)
                nextKey = graph[key][0]
                if len(graph[key]) > 1:
                    graph[key].remove(nextKey)
                else:
                    graph.pop(key)
                key = nextKey
                if not outs.has_key(key) or len(outs[key]) > 1 or not ins.has_key(key) or len(ins[key]) > 1:
                    break
            contig.append(key)
            
            key = start_key
            while ins.has_key(key) and len(ins[key]) == 1 and outs.has_key(key) and len(outs[key]) == 1:
                prevKey = ins[key][0]
                contig.insert(0,prevKey)
                if graph.has_key(prevKey):
                    if len(graph[prevKey]) > 1:
                        graph[prevKey].remove(key)
                    else:
                        graph.pop(prevKey)
                key = prevKey
            
            #print contig
            contigs.append(self.printCycle(contig))
        contigs.sort()
        return contigs
    
    
    def deBruijnKmer(self,kmers):
        graph = {}
        for kmer in kmers:
            if not graph.has_key(kmer[:-1]):
                graph[kmer[:-1]] = [kmer[1:]]
            else:
                graph[kmer[:-1]].append(kmer[1:])
        return graph
    
    def findBalance(self,graph):
        ins = {}
        outs = {}
        for key in graph:
            outs[key] = graph[key][:]
            for end in graph[key]:
                if not ins.has_key(end):
                    ins[end] = [key]
                else:
                    ins[end].append(key)
        return (ins,outs)
    
    def printCycle(self,cycle):
        k = len(cycle[0])
        out = cycle[0]
        for node in cycle[1:]:
            if out[len(out)-k+1:] == node[:-1]:
                out += node[-1]
        return out
    
        
if __name__ == "__main__":
    p42 = Problem42()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_4jjj.txt",'r')
    line = in_file.readline().strip()

    kmers = []
    while line and line != "":
        kmers.append(line)
        line = in_file.readline().strip()
    
    out_file = open("prob42_out.txt",'w')
    out = p42.contigGeneration(kmers)

    for contig in out:
        #print contig,
        out_file.write(contig+" ")
    out_file.flush()
    
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"