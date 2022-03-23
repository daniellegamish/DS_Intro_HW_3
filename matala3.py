# -*- coding: utf-8 -*-
"""
Danielle Gamish

205454127
"""
#A:
def  read_line(n, file):
    
    if not isinstance(n, int):
       return('invalid input')  

    if file != "C:/Users/danie/.spyder-py3/matala_3/ex3_text.txt":
        return('file not found')    

    count = 0
    file = open(file)
    for line in file:
        count += 1       
        if count == n:
            return(line)
        
    if n > count:
        num = str(n)
        return("line " + num + " doesn't exist")

#B:

import re

def longest_words(file):
    lst_result = []    
    if file != "C:/Users/danie/.spyder-py3/matala_3/ex3_text.txt":
        print('file not found')
        return(lst_result)
    
    file = open('C:/Users/danie/.spyder-py3/matala_3/ex3_text.txt')     
    counts = {}
    for line in file:
        words = line.split()
        words = re.split('[\s+ . , )]', line)  
        for word in words:
            if word.isalpha(): 
                counts[word] = (len(word))
           
    lst = sorted(counts.items(), key=lambda x: x[1], reverse=True)       
    for val, key in lst[:5]:
        lst_result.append(val)
    return(lst_result)         