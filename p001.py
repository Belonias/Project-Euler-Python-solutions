# Multiples of 3 and 5
# Problem 1
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
# Import time module to count time
import time
start_time = time.time()

# Import argv module to take the name of the script
from sys import argv

# Replace .py extension with -answer.txt
# for the new answer txt file
script = argv
answer_txt = script.pop(0)
answer_txt = answer_txt.replace('.py','-answer.txt')

# Setup the the sum variable
the_sum = 0

# For loop to check the numbers between 1 and 1000
for number in range(1,1000):
# Check with mod(%) if the remainder is 0
    if number % 3 == 0 or number % 5 == 0:
# Add the number to the_sum variable
        the_sum += number

# Print the answer
print("\nThe answer is %d\n" % the_sum)
# Open a new txt file with the name of the script + -answer
# end txt extension
txt = open(answer_txt, 'w')
# Write the answer of the problem and
# the time to execution
txt.write("The answer is " + str(the_sum) + "\nExecuted in " + str(time.time() - start_time) + " seconds")
# Save the txt file
txt.close
