# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:20:47 2014

@author: Jeffrey
"""

import time, sys

class Problem38:
    
    def eulerianPath(self,strEdges):
        graph = self.processGraph(strEdges)
        (ins,outs) = self.findBalance(graph)
        startNode = -1
        endNode = -1
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
        return self.printCycle(self.condenseCycle(total_cycle))
    
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
        out = str(cycle[0])
        for node in cycle[1:]:
            out += "->" + str(node)
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
            start = int(nodes[0])
            ends = map(int,nodes[2].split(","))
            edges[start] = ends
        return edges
        
if __name__ == "__main__":
    p38 = Problem38()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_4ff.txt",'r')
    line = in_file.readline().strip()
    
    strEdges = []
    while line and line != "":
        strEdges.append(line)
        line = in_file.readline().strip()
    
    out_file = open("prob38_out.txt",'w')
    out = p38.eulerianPath(strEdges)

    print out
    out_file.write(out+"\n")
    out_file.flush()
    
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"