# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 01:47:40 2014

@author: Jeffrey
"""


import sys,time

class Node:
    
    def __init__(self,parent,parent_string,root_distance):
        self.parent_ = parent
        self.parent_string_ = parent_string
        self.children_ = []
        self.children_strings_ = []
        self.root_distance_ = root_distance
        
    def addChild(self,child,child_string):
        self.children_.append(child)
        self.children_strings_.append(child_string)
    
    def changeParent(self,new_parent,new_parent_string):
        self.parent_ = new_parent
        self.parent_string_ = new_parent_string
    

class Problem50:
    
    def array2tree(self,text,array,lcp):
        root = Node(None,None,0)
        prevNode = root
        for i in xrange(len(array)):
            if lcp[i] == 0:
                currString = text[array[i]:]
                currNode = Node(root,currString,len(currString))
                root.addChild(currNode,currString)
                prevNode = currNode
            else:
                currNode = prevNode
                while lcp[i] < currNode.root_distance_:
                    currNode = currNode.parent_
                rd = currNode.root_distance_
                if lcp[i] == rd:
                    childString = text[array[i]+lcp[i]:]
                    currNode.addChild(Node(currNode,childString,len(text[array[i]:])),childString)
                    
                    prevNode = currNode
                else:
                    currChild = currNode.children_.pop()
                    currChildString = currNode.children_strings_.pop()
                    newString = currChildString[:lcp[i]-rd]
                    newNode = Node(currNode,newString,lcp[i])
                    currNode.addChild(newNode,newString)
                    newChildString = currChildString[lcp[i]-rd:]
                    currChild.changeParent(newNode,newChildString)
                    newNode.addChild(currChild,newChildString)
                    leafString = text[array[i]+lcp[i]:]
                    newNode.addChild(Node(newNode,leafString,len(text[array[i]])),leafString)
                    
                    prevNode = newNode
                    
        leavesLeft = [root]
        output = []
        while leavesLeft:
            currNode = leavesLeft.pop()
            for i in xrange(len(currNode.children_)):
                leavesLeft.append(currNode.children_[i])
                output.append(currNode.children_strings_[i])
        return output
    
        
if __name__ == "__main__":
    p50 = Problem50()
    sys.setrecursionlimit(100000)
    
    start_time = time.time()
    
    in_file = open("rosalind_7h.txt",'r')    
    text = in_file.readline().strip()
    
    suff_array_str = in_file.readline().strip()
    lcp_str = in_file.readline().strip()
    
    suff_array = map(int,suff_array_str.split(', '))
    lcp = map(int,lcp_str.split(', '))

    
    out_file = open("prob50_out.txt",'w')
    out = p50.array2tree(text,suff_array,lcp)

    for i in out:
        print i
        out_file.write(i+'\n')
    out_file.flush()

    out_file.close()
    in_file.close()
    print time.time() - start_time, "seconds"