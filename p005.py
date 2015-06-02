# Project Euler
# Smallest multiple
# Problem 5

'''
2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number 
that is evenly divisible by all of the numbers from 1 to 20?
'''
import time
from sys import argv

script = argv
answer_txt = script.pop(0)
answer_txt = answer_txt.replace('.py', '-answer.txt')

start_time = time.time()

step_1 = 20
step_2 = 2520

while step_1 > 10:
    if step_2 % step_1 == 0:
        step_1 -= 1
    else:
        step_2 += 1
        step_1 = 20

print("The answer is %d" % (step_2), 
      "\nElapsed Time %.2f" % (time.time() - start_time))

with open(answer_txt, 'w') as txt:
    txt.write("The answer is %d" % (step_2) + 
      "\nElapsed Time %.2f" % (time.time() - start_time))
