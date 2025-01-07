# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:20:43 2014

@author: Jeffrey
"""



import time, sys

class Problem37:
    
    def eulerianCycle(self,graph):
        total_cycle = []
        while graph:
            cycle = []
            start_key = graph.keys()[-1]
            key = start_key
            while graph and graph.has_key(key):
                cycle.append(key)
                nextKey = graph[key].pop()
                while nextKey == start_key and graph[key]:
                    nextKey = graph[key].pop()
                    graph[key].append(start_key)
                if not graph[key]:
                    graph.pop(key)
                key = nextKey
            cycle.append(key)
            total_cycle.append(cycle)
        
        return self.printCycle(self.condenseCycle(total_cycle))
    
    def printCycle(self,cycle):
        out = str(cycle[0])
        for node in cycle[1:]:
            out += "->" + str(node)
        return out
    
    def condenseCycle(self,total_cycle):
        output = []
        output = total_cycle.pop(0)
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
    p37 = Problem37()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_4ee.txt",'r')
    line = in_file.readline().strip()
    
    strEdges = []
    while line and line != "":
        strEdges.append(line)
        line = in_file.readline().strip()
    
    out_file = open("prob37_out.txt",'w')
    graph = p37.processGraph(strEdges)
    out = p37.eulerianCycle(graph)

    print out
    out_file.write(out+"\n")
    out_file.flush()
    
    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"