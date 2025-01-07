# -*- coding: utf-8 -*-
"""
Created on Sun Feb 02 12:24:23 2014

@author: Jeffrey
"""

import time, sys

class Problem23:
    
    def dagLongPath(self,source,sink,edges):
        scores = [0 for x in range(source,sink+1)]
        backtrack = [-1 for x in range(source,sink+1)]
        nodes = [source]
        while nodes:
            i = nodes.pop(0)
            if edges.has_key(i):
                for (end,weight) in edges[i]:
                    if end <= sink:
                        nodes.append(end)
                        if scores[end-source] < scores[i-source]+weight:
                            scores[end-source] = scores[i-source]+weight
                            backtrack[end-source] = i
                            
        i = sink
        out = str(sink)
        while i != source and i >= 0:
            out = str(backtrack[i-source])+"->"+out
            i = backtrack[i-source]
        return (scores[sink-source]-scores[source-source],out)
    
if __name__ == "__main__":
    p23 = Problem23()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    in_file = open("rosalind_5dd.txt",'r')
    source = int(in_file.readline().strip())
    sink = int(in_file.readline().strip())
    edges = {}
    line = in_file.readline().strip()
    while line and line != "":
        parts = line.split(":")
        nodes = parts[0].split("->")
        if not edges.has_key(int(nodes[0])):
            edges[int(nodes[0])] = [(int(nodes[1]),int(parts[1]))]
        else:
            edges[int(nodes[0])].append((int(nodes[1]),int(parts[1])))
        line = in_file.readline().strip()

    out_file = open("prob23_out.txt",'w')
    
    print edges
    
    (score,path) = p23.dagLongPath(source,sink,edges)
    print score
    print path
    out_file.write(str(score)+"\n")
    out_file.write(path)
    out_file.flush()
    print time.time() - start_time, "seconds"