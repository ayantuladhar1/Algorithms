# Name: Ayan Tuladhar


import time

# The following program represents naive LCS recursive Python implementation of LCS.
# This function finds the length of longest subsequence present in the given sequence,


def recursive_implementation_for_lcs(a, b, c, d):
    # Here a and b are given sequences.
    if a == -1 or b == -1:
        return 0
    # Checks if there is a match.
    if c[a] == d[b]:
        return recursive_implementation_for_lcs(a-1, b-1, c, d)+1
    # Returns if there is no match found.
    return max(recursive_implementation_for_lcs(a-1, b, c, d), recursive_implementation_for_lcs(a, b-1, c, d))

# The following function was compiled from module "CSCI 3412 Module 14 Dynamic Programming.pptx"(Slide - 31).
# The following function represents Dynamic Programming for Longest Common Sequence with bottom-up version.
# The following function is also a representation of Dynamic Programming Python implementation with memoization.


def dynamic_programming_for_long_common_sequence(c, d):
    # Here a and b are local variables.
    a = len(c)
    b = len(d)
    # Stores the dp values and declares the array.
    # First it creates all entries of long_common_sequence table to 0.
    long_common_sequence = [[0 for i in range(b+1)] for i in range(a+1)]
    for x in range(1, a+1):
        for y in range(1, b+1):
            # Checks if there is a match.
            if c[x-1] == d[y-1]:
                long_common_sequence[x][y] = long_common_sequence[x-1][y-1]+1
            # Moves on if there is no match found.
            else:
                long_common_sequence[x][y] = max(long_common_sequence[x-1][y], long_common_sequence[x][y-1])
    return long_common_sequence[a][b]

# The following function represents driver program for naive recursive LCS, LCS DP and bottom-up version.
# The following driver program reads all the numbers in "rand1000000.txt" file as strings where for each -
# 6- digit integer string in the file it run an LCS function against "0123456789".


# To read the 1M integers from file "rand1000000.txt"
file = open('rand1000000.txt', 'r')

# Creates index as list to store 6 digit integers.
index = []
for line in file:
    for integer in line.split():
        # Checks the condition where the integers are 6 digit.
        if len(integer) == 6:
            index.append(integer)
recursive_total_time = 0

# The following time efficiency function was compiled from HW2.
# The following function compares the time efficiency of recursive algorithm for 1M integer strings.
for integer in index:
    start_time = time.time()
    recursive_implementation_for_lcs(len(integer)-1, 9, integer, '0123456789')
    end_time = time.time()
    recursive_total_time = recursive_total_time + (end_time-start_time)
print('The result below displays the total time efficiency for LCS naive recursive:')
print(recursive_total_time, "seconds")

# The following time efficiency function was compiled from HW2.
# The following function compares the time efficiency of LCS DP bottom up version for 1M integer strings.

dynamic_programming_total_time = 0
for integer in index:
    start_time = time.time()
    dynamic_programming_for_long_common_sequence(integer, '0123456789')
    end_time = time.time()
    dynamic_programming_total_time = dynamic_programming_total_time + (end_time-start_time)
print('The result below displays the total time efficiency for LCD DP bottom up version:')
print(dynamic_programming_total_time, "seconds")

