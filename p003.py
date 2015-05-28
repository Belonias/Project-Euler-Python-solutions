# Project Euler
# Largest prime factor
# Problem 3

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import time
from sys import argv

script = argv
answer_txt = script.pop(0)
answer_txt = answer_txt.replace('.py', '-answer.txt')

prime_factor_list = []
z = 1

number = int(input("Number: "))
start_time = time.time()

for i in range(2, number):

    if number % i == 0:

        prime_factor_list.append(i)
        z *= i

        if z > number: break

prime_factor_list.pop()
            
print("The answer is", prime_factor_list[-1], "\nElapsed Time %.2f seconds" % (time.time() - start_time))

with open(answer_txt, 'w') as txt:
    txt.write("The answer is " + str(prime_factor_list[-1]) + 
              "\nElapsed Time " + str(time.time() - start_time) + " seconds\n")
