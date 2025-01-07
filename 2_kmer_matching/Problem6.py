# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 19:12:06 2014

@author: Jeffrey
"""

class ReverseComp:
    
    def revComp(self,string):
        out = ""
        for c in string:
            if c == "A":
                out += "T"
            elif c == "C":
                out += "G"
            elif c == "G":
                out += "C"
            elif c == "T":
                out += "A"
            else:
                pass
        return out[::-1]

if __name__ == "__main__":
    rc = ReverseComp()
    in_file = open("rosalind_1c.txt",'r')
    seq = in_file.read()
    out_file = open("prob6_out.txt",'w')
    out_file.write(rc.revComp(seq))
    out_file.flush()
            