import time
from sys import argv

script = argv
answer_txt = script.pop(0)
answer_txt = answer_txt.replace('.py', '-answer.txt')

start_time = time.time()

difference = 0
SumOfTheSquares = 0
SquareOfTheSum = 0

for i in range(1, 101):
    SumOfTheSquares += i * i


for i in range(1, 101):
    SquareOfTheSum += i

SquareOfTheSum **= 2

difference = SquareOfTheSum - SumOfTheSquares

print("The answer is %d" % (difference), 
      "\nElapsed Time %.2f" % (time.time() - start_time))

with open(answer_txt, 'w') as txt:
    txt.write("The answer is %d" % (difference) + 
      "\nElapsed Time %.2f" % (time.time() - start_time))
