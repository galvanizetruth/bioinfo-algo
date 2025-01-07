# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:30:57 2014

@author: Jeffrey
"""


import time, sys

class Problem40:
    
    def kUniversalString(self,k):
        kmers = self.allKmers(k,[])
        graph = self.deBruijnKmer(kmers)
        
        '''
        (ins,outs) = self.findBalance(graph)
        startNode = ""
        endNode = ""
        for key in graph:
            if not ins.has_key(key) or ins[key] < outs[key]:
                startNode = key
            elif not outs.has_key(key) or ins[key] > outs[key]:
                endNode = key'''
        total_cycle = []
        first = True
        while graph:
            cycle = []
            start_key = graph.keys()[0]
            
            '''if first:
                start_key = startNode
                first = False'''
            key = start_key
            while graph and graph.has_key(key):
                cycle.append(key)
                nextKey = graph[key].pop(0)
                while nextKey == start_key and graph[key]:
                    nextKey = graph[key].pop(0)
                    graph[key].append(start_key)
                if not graph[key]:
                    graph.pop(key)
                key = nextKey
            cycle.append(key)
            total_cycle.append(cycle)
        #print total_cycle
        return self.printCycle(self.condenseCycle(total_cycle))
    
    def allKmers(self,k,out):
        '''Returns all kmers of length k'''
        if out == []:
            return self.allKmers(k,['0','1'])
        else:
            if len(out[0]) == k:
                return out
            else:
                res = []
                bases = ['0','1']
                for s in out:
                    for b in bases:
                        res.append(s+b)
                return self.allKmers(k,res)
    
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
            outs[key] = graph[key]
            for end in graph[key]:
                if not ins.has_key(end):
                    ins[end] = [key]
                else:
                    ins[end].append(key)
        return (ins,outs)
    
    def printCycle(self,cycle):
        k = len(cycle[0])
        out = cycle[0]
        for node in cycle[1:-1*k]:
            if out[len(out)-k+1:] == node[:-1]:
                out += node[-1]
        return out
    
    def condenseCycle(self,total_cycle):
        output = []
        for cycle in total_cycle:
            if cycle[0] != cycle[-1]:
                output = cycle
        if not output:
            output = total_cycle[0][:]
        total_cycle.remove(output)
        while total_cycle and len(total_cycle) >= 1:
            cycle = total_cycle.pop(0)
            temp = self.addCycle(output,cycle)
            if not temp:
                total_cycle.append(cycle)
            else:
                output = temp
        return output
    
    def addCycle(self,cycle1,cycle2):
        out = []
        for i in range(len(cycle1)):
            if cycle1[i] in cycle2:
                ind = cycle2.index(cycle1[i])
                out = cycle1[:i] + cycle2[ind:]+cycle2[1:ind+1] + cycle1[i+1:]
                return out
    
    def processGraph(self,strEdges):
        edges = {}
        for s in strEdges:
            nodes = s.split(" ")
            start = nodes[0]
            ends = nodes[2].split(",")
            edges[start] = ends
        return edges
        
if __name__ == "__main__":
    p40 = Problem40()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    #in_file = open("rosalind_4htest.txt",'r')
    #k = int(in_file.readline().strip())
    k = 18
    '''
    strEdges = []
    while line and line != "":
        strEdges.append(line)
        line = in_file.readline().strip()
    '''
    out_file = open("prob40_out.txt",'w')
    out = p40.kUniversalString(k)

    print out
    out_file.write(out+"\n")
    out_file.flush()
    
    out_file.close()
    #in_file.close()
    print time.time() - start_time, "seconds"