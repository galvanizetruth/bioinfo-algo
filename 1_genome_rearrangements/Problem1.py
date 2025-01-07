# -*- coding: utf-8 -*-
"""
Created on Thu Jan 09 22:33:13 2014

@author: Jeffrey
"""

class CSE282_HW1:
    
    def greedySorting(self, P):
        '''Input: a signed permutation P in format (-1 -2 +3 +4) with signed
        numerical values from 1 to n
        Output: the sequence of permutations corresponding to applying
        GreedySorting to P, ending with the identity permutation'''
        
        lst = self.permToList(P)
        identity = [x+1 for x in range(len(lst))]
        i = 0
        while lst != identity:
            #i+1 is the value that should be in lst[i]
            if lst[i] != i+1:
                bpoint = self.findIndex(lst,i+1)+1
                lst = self.reversal(lst,i,bpoint)
                print self.listToPerm(lst)
            else:
                i += 1
            
    def permToList(self, perm):
        '''Input: a signed permutation, perm, in format (-1 -2 +3 +4)
        Output: a list of the same permutation, in format [-1,-2,3,4]'''
        
        return map(int,perm[1:len(perm)-1].split(" "))
    
    def findIndex(self, lst, value):
        '''Input: a signed integer list, lst, and a signed integer, value,
        whose magnitude corresponds to that of one of the integers in lst
        Output: the first index of lst whose magnitude corresponds to value's,
        otherwise, returns -1'''
        
        for i in range(len(lst)):
            if abs(lst[i]) == abs(value):
                return i
        return -1
    
    def reversal(self, lst, i1, i2):
        '''Input: a list of signed integers, lst, and two indices, i1 and i2,
        which are the breakpoints for the reversal
        Output: the same list with the integers in between i1 and i2 reversed,
        i.e. the order of the numbers are reversed and their signs are flipped'''
        
        if i1 == 0:
            return map(lambda x: -x, lst[i2-1::-1]) +lst[i2:]
        elif i2 == len(lst):
            return lst[0:i1] + map(lambda x: -x, lst[:i1-1:-1])
        else:
            return lst[0:i1] + map(lambda x: -x, lst[i2-1:i1-1:-1]) +lst[i2:]
        
    def listToPerm(self, lst):
        '''Input: a list of a signed permutation, in format [-1,-2,3,4]
        Output: the same signed permutation as a string, (-1 -2 +3 +4)'''

        out = "("        
        for num in lst:
            if num > 0:
                out += "+"
            out += str(num) + " "
        out = out[:len(out)-1]+")"
        return out
        
if __name__ == "__main__":
    hw1 = CSE282_HW1()
    hw1.greedySorting("(-69 +54 +156 +183 -30 +191 -293 +12 -265 +116 -15 +202 -11 -317 +237 -307 -209 +5 -193 +37 +8 -238 -159 -217 +219 -6 -38 +19 -90 -167 +289 +226 -2 -115 -264 +157 -262 -73 -76 +155 -125 +55 -124 -26 +258 -298 +160 -161 -211 -178 -252 -190 -40 -200 -166 +185 -208 +111 +13 -93 +256 -144 -303 -158 +304 +14 +198 -197 +240 -118 +312 +91 -206 +140 +43 +267 -79 +35 -18 -272 -68 +175 +130 -212 +142 -271 -220 -96 -77 +245 -173 -24 +4 -63 -3 -100 -57 -184 +291 -36 +218 +301 -283 -148 +314 -257 +244 -134 +81 -222 -109 -270 +310 -82 +123 -261 -234 +236 -75 +25 -138 +106 -65 +104 +141 +52 +29 -101 -33 +80 -154 -58 +228 -300 -99 +163 -126 -253 -7 -74 -9 +146 -71 -94 -70 -50 +279 -315 +49 +180 -21 +288 -273 +316 -243 +216 +83 +88 -117 -139 +195 -60 +225 +247 -32 -259 -112 -242 -266 -46 +294 -62 -132 +162 +199 +169 +281 -176 +120 -152 -233 +102 -67 +92 +131 +235 +282 -59 -113 -230 +249 +286 -42 -189 +87 -299 -108 -268 +98 +84 +192 -284 +224 -78 -129 +41 -64 +27 -290 +22 +251 +34 +164 +254 +47 -17 +285 -1 -150 -168 +143 +276 -275 -196 +45 +135 +182 +181 -210 -114 -174 -151 +172 -306 -31 -274 -255 +250 +246 +269 -133 -48 +177 -28 -103 +213 +287 -23 +232 -311 +97 -278 -89 +280 +215 +110 -296 -145 +309 -277 -137 -305 +105 +122 +170 +128 +10 +136 +186 -72 -86 +61 +44 +297 -214 +39 +221 +66 +119 +153 -239 +147 -295 -308 +204 -188 -194 +165 -127 -95 +51 +263 -260 -107 +292 -53 -205 +16 +302 -121 -229 +56 -203 +207 -231 -85 +179 +223 -20 -201 +248 +313 -227 -187 -171 +149 -241)")
