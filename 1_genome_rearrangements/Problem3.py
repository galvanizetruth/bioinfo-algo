# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 13:33:22 2014

@author: Jeffrey
"""

class CSE282_Prob3:

    def twoBreakDistance(self, p, q):
        '''Input: Two genomes represented by sets of signed permutations, p and q
        Output: The two break distance between p and q'''
        
        #in_file = open("rosalind_6c.txt",'r')
        #p = in_file.readline()
        #q = in_file.readline()
        #print q
        g1 = self.permToList(p)
        g2 = self.permToList(q)
        print g1,g2
        
        ### Let 1 be the input of +1, 2 be the output of +1,
        ### 3 be the input of +2, 4 be the output of +2, etc.
        length = 0
        for chrom in g1:
            length += len(chrom)
        #Length is the total number of synteny blocks, equal to n in 1,...,n
        bp_graph = [[0,0] for x in range(length*2)]
        #Make the breakpoint graph: index 0 is [11,8] which means that
        #the output of 6 goes to 1 in g1 and the input of 5 goes to 1 in g2
        for chrom in g1:
            for i in range(-1,len(chrom)-1):
                #If there is a positive value at i, the outward edge of i is to i+1
                #and the inward edge is to i-1 - not shown here
                if chrom[i] > 0:
                    #If it goes to a positive number, it enters at the input
                    if(chrom[i+1]) > 0:
                        #Zero indexed so 2*chrom[i]-1 is inward edge
                        bp_graph[2*abs(chrom[i])-1][0] = 2*abs(chrom[i+1])-2
                        bp_graph[2*abs(chrom[i+1])-2][0] = 2*abs(chrom[i])-1
                    #if it goes to a negative number, it enters at the output
                    else:
                        bp_graph[2*abs(chrom[i])-1][0] = 2*abs(chrom[i+1])-1
                        bp_graph[2*abs(chrom[i+1])-1][0] = 2*abs(chrom[i])-1
                #If there is a negative value at i, the inward edge of i goes to i+1
                else:
                    if(chrom[i+1]) > 0:
                        bp_graph[2*abs(chrom[i])-2][0] = 2*abs(chrom[i+1])-2
                        bp_graph[2*abs(chrom[i+1])-2][0] = 2*abs(chrom[i])-2
                    else:
                        bp_graph[2*abs(chrom[i])-2][0] = 2*abs(chrom[i+1])-1
                        bp_graph[2*abs(chrom[i+1])-1][0] = 2*abs(chrom[i])-2
        #Same as above, but with the second array == 1.
        for chrom in g2:
            for i in range(-1,len(chrom)-1):
                if chrom[i] > 0:
                    if(chrom[i+1]) > 0:
                        bp_graph[2*abs(chrom[i])-1][1] = 2*abs(chrom[i+1])-2
                        bp_graph[2*abs(chrom[i+1])-2][1] = 2*abs(chrom[i])-1
                    else:
                        bp_graph[2*abs(chrom[i])-1][1] = 2*abs(chrom[i+1])-1
                        bp_graph[2*abs(chrom[i+1])-1][1] = 2*abs(chrom[i])-1
                else:
                    if(chrom[i+1]) > 0:
                        bp_graph[2*abs(chrom[i])-2][1] = 2*abs(chrom[i+1])-2
                        bp_graph[2*abs(chrom[i+1])-2][1] = 2*abs(chrom[i])-2
                    else:
                        bp_graph[2*abs(chrom[i])-2][1] = 2*abs(chrom[i+1])-1
                        bp_graph[2*abs(chrom[i+1])-1][1] = 2*abs(chrom[i])-2
        copy_graph = list(bp_graph)
        num_cycles = 0
        from_node = 0
        #Traverse the bp_graph, popping values as you go, referring to
        #copy_graph for the indices
        while bp_graph:
            print bp_graph
            start = bp_graph[0][0]
            edge = bp_graph[0][1]
            bp_graph.pop(0)
            i = 0
            j = 1
            
            #One iteration is one cycle
            while edge != start:
                bp_graph.remove([copy_graph[edge][0],copy_graph[edge][1]])
                from_node = edge
                edge = copy_graph[edge][i]
                #Toggle back and forth between 0 and 1
                k = i
                i = j
                j = k
            else:
                bp_graph.remove([copy_graph[edge][0],copy_graph[edge][1]])
            num_cycles += 1
                    
        return length - num_cycles
        
        
    
    def permToList(self, perm):
        '''Input: a signed permutation, perm, in format (-1 -2 +3 +4)(+5 +6)
        Output: a list of the same permutation, in format [[-1,-2,3,4][5,6]]'''
        #if perm[-1] != ")":
        #    return map(lambda x:map(int,x.split(" ")),perm[1:len(perm)-2].split(')('))
        #else:
        return map(lambda x:map(int,x.split(" ")),perm[1:len(perm)-1].split(')('))

                

if __name__ == "__main__":
    p3 = CSE282_Prob3()
    #print p3.permToList("(+1 -3 -6 -5 +2 -4)")
    print p3.twoBreakDistance("(+1 +2 +3 +4 +5 +6)","(+1 -3 -6 -5)(+2 -4)")
    