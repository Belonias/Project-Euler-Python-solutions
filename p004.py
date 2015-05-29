# Project Euler
# Largest palindrome product
# Problem 4

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import time
from sys import argv

script = argv
answer_txt = script.pop(0)
answer_txt = answer_txt.replace('.py', '-answer.txt')

start_time = time.time()
palindrome_list = []
palindrome_check = None
            
for i in range(999,99,-1):
    for j in range(999,99,-1):
        palindrome_check = i * j
        if str(palindrome_check) == str(palindrome_check)[::-1]:
            palindrome_list.append(palindrome_check)

print("The answer is", max(palindrome_list), "\nElapsed Time %.2f seconds" %(time.time()-start_time))

with open(answer_txt, 'w') as txt:
    txt.write("The answer is " + str(max(palindrome_list)) + "\nElapsed Time " + str(time.time()-start_time) + " seconds")
