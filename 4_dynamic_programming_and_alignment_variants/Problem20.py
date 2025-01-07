# -*- coding: utf-8 -*-
"""
Created on Sat Feb 01 00:21:45 2014

@author: Jeffrey
"""

import time

class Problem20:
    
    def change(self,money,coins):
        minNumChange = [money + 1 for x in range(money+1)]
        minNumChange[0] = 0
        for i in range(1,money+1):
            for coin in coins:
                if i >= coin:
                    if minNumChange[i-coin] + 1 < minNumChange[i]:
                        minNumChange[i] = minNumChange[i-coin]+1
        return minNumChange[money]
        
    def changeRecur(self,money,coins,num):
        if money == 0:
            return num
        else:
            counts = [money]
            for coin in coins:
                if coin == money:
                    return num + 1
                elif coin < money:
                    counts.append(self.changeRecur(money - coin,coins,num+1))
            return min(counts)
        
    
if __name__ == "__main__":
    p20 = Problem20()
    
    start_time = time.time()
    in_file = open("rosalind_5a.txt",'r')
    money = int(in_file.readline().strip())
    coins = in_file.readline().strip().split(",")
    coins = map(int,coins)

    out_file = open("prob20_out.txt",'w')
    
    out = p20.change(money,coins)
    print out
    out_file.write(str(out))
    out_file.flush()
    print time.time() - start_time, "seconds"