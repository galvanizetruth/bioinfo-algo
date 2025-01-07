# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 02:46:25 2014

@author: Jeffrey
"""

import time, sys

class Problem41:
    
    def readPairStringReconstruction(self,d,strPairedReads):
        kmers = self.processGraph(strPairedReads)
        graph = self.deBruijnKmer(kmers)
        #print graph
        (ins,outs) = self.findBalance(graph)
        startNode = ""
        endNode = ""
        for key in graph:
            if not ins.has_key(key) or ins[key] < outs[key]:
                startNode = key
            elif not outs.has_key(key) or ins[key] > outs[key]:
                endNode = key
        total_cycle = []
        first = True
        while graph:
            cycle = []
            start_key = graph.keys()[0]
            
            if first:
                start_key = startNode
                first = False
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
        #print
        #print self.condenseCycle(total_cycle)
        return self.printCycle(d,self.condenseCycle(total_cycle))
    
    
    def deBruijnKmer(self,kmers):
        graph = {}
        for pair in kmers:
            if not graph.has_key((pair[0][:-1],pair[1][:-1])):
                graph[(pair[0][:-1],pair[1][:-1])] = [(pair[0][1:],pair[1][1:])]
            else:
                graph[(pair[0][:-1],pair[1][:-1])].append((pair[0][1:],pair[1][1:]))
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
    
    def printCycle(self,d,cycle):
        k = len(cycle[0][0])
        out = cycle[0][0]
        out2 = cycle[0][1]
        for node in cycle[1:]:
            if out[len(out)-k+1:] == node[0][:-1]:
                out += node[0][-1]
            if out2[len(out2)-k+1:] == node[1][:-1]:
                out2 += node[1][-1]
        if out[k+1+d:] == out2[:len(out)-k-1-d]:
            out2 = out2[len(out)-k-1-d:]
        return out+out2
    
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
    
    def processGraph(self,strPairedReads):
        edges = []
        for s in strPairedReads:
            edges.append(s.split("|"))

        return edges
        
if __name__ == "__main__":
    p41 = Problem41()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_4ii.txt",'r')
    d = int(in_file.readline().strip())
    line = in_file.readline().strip()
    
    strEdges = []
    while line and line != "":
        strEdges.append(line)
        line = in_file.readline().strip()
    
    out_file = open("prob41_out.txt",'w')
    out = p41.readPairStringReconstruction(d,strEdges)

    print out
    out_file.write(out+"\n")
    out_file.flush()
    
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"