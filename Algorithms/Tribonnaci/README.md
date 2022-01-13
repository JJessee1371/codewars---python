# Date
Jan 13, 2022

# Description
Each new number of the Fibonnaci sequence is determined by summing the last two numbers in the sequence together. 
This challenge is looking to accomplish a similar task, but by summing the last three numbers in the sequence. 

# Task
Given a signature of 3 numbers e.g. [1, 1, 1] and a variable n. Return the first n numbers in the sequence,
including the original signature. 

# Rules
n will always ne a non-negative number.
If n == 0, return an empty array. 


# Things I learned
- I was not aware that there was a sum method, that would have shortened my addition.
- res[-3:] was a clever trick, until today I had not seen negative indexes used. 
- I knew that there must be a shorter way to reach my solution, given some more time to
    become familiar with the Python methods I feel confident in my ability to reach 
    more concise solutions. 