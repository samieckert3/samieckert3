# -*- coding: utf-8 -*-
"""
Spyder Editor
"""

def my_dec_2_bin(d):
    '''d is a positive integer''' 
    d = int(d)
    bin_out = []
    if d == 0:
        
        return [0]
    
    elif d == 1:
        
        return [1]
    
    else:
        
        leading_one = False
        
        while leading_one == False:
            
            remainder = d % 2
            d = d // 2
            bin_out.insert(0, remainder)
            
            if d == 1:
            
                bin_out.insert(0, 1)         
                leading_one = True
    
        return bin_out 


my_dec_2_bin(0)

def my_bin_2_dec(b):

    dec = 0
    i = 0
    
    
    while i < len(b):
        if i == 0:
            dec = 1
            i += 1
        else:
            dec = (dec * 2) + b[i]
            i += 1
    return dec

print(my_bin_2_dec(my_dec_2_bin(12654)))