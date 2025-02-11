# Fibonacci Series: The Fibonacci Sequence is a series of numbers starting with 0 and 1, where each succeeding number is the sum of the two preceding numbers. The sequence goes on infinitely.
# The sequence begins as: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …

# CODE:-
firstnum = 0
secondnum = 1
print(firstnum)
print(secondnum)
for i in range(1, 20):
    nextnum = firstnum + secondnum
    print(nextnum, end='  ')
    firstnum = secondnum
    secondnum = nextnum

# Explanation: We initialize the first number as 0 and the second number as 1. For the Fibonacci series, 
# each number is the sum of the two preceding numbers. To achieve this, we use an extra variable named 'nextnum', 
# which stores the sum of 'firstnum' and 'secondnum' (i.e., nextnum = firstnum + secondnum). This value is then updated for the next iteration.

