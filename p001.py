# Project Euler
# Multiples of 3 and 5
# Problem 1
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
import time
start_time = time.time()

from sys import argv

# Replace .py extension with -answer.txt 
script = argv
answer_txt = script.pop(0)
answer_txt = answer_txt.replace('.py','-answer.txt')

the_sum = 0

for number in range(1,1000):
    if number % 3 == 0 or number % 5 == 0:
        the_sum += number

print("\nThe answer is %d\n" % the_sum)
txt = open(answer_txt, 'w')
txt.write("The answer is " + str(the_sum) + "\nElapsed Time " + str(time.time() - start_time) + " seconds\n")
txt.close
