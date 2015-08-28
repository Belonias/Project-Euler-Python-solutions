import time
from sys import argv

script = argv
answer_txt = script.pop(0)
answer_txt = answer_txt.replace('.py', '-answer.txt')

start_time = time.time()

def findPrime(PrimeList, number):
    flag = True
    for i in range(2,number):
        if number % i == 0:
            flag = False
            break
        else:
            pass
    if flag:
        PrimeList.append(number)
    return PrimeList

number = 2
PrimeList = [2]

while len(PrimeList) < 10001:
    number += 1
    findPrime(PrimeList, number)

print("The answer is %d" % (PrimeList[-1]), 
      "\nElapsed Time %.2f" % (time.time() - start_time))

with open(answer_txt, 'w') as txt:
    txt.write("The answer is %d" % (PrimeList[-1]) + 
      "\nElapsed Time %.2f" % (time.time() - start_time))
