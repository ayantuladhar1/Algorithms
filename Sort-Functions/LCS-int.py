# Name: Ayan Tuladhar


# To read the 1M integers from file "rand1000000.txt"
file = open('rand1000000.txt', 'r')
with open('rand1000000.txt', 'r') as integers_infile:
    Index = [integers.rstrip() for integers in integers_infile.readlines()]
file.close()

# The following function is the modified version of naive recursive LCS.


def lowest_common_sequence(a, b, c, d):
    # Here c and d are the given sequences.
    if c == 0 or d == 0:
        return 1, 0
    # checks if there is a match.
    elif a[c - 1] == b[d - 1]:
        i, j = lowest_common_sequence(a, b, c - 1, d - 1)
        return (i + 1), (j + 1)
    else:
        i1, j1 = lowest_common_sequence(a, b, c, d - 1)
        i2, j2 = lowest_common_sequence(a, b, c - 1, d)
        if j1 > j2:
            return (i1 + i2 + 1), j1
        else:
            return (i1 + i2 + 1), j2


# The following function counts the number of recursive calls for each 6-digit integer string-
# (100,000-999,999) against "0123456789" string and returns a tuple of two elements -
# LCS num and The number of recursive calls to find the LCS.
for integers in Index:
    p, q = lowest_common_sequence(integers, '0123456789', 6, 10)
    print("The LCS num for %s = %d\n"
          "The number of recursive calls to find LCS = %d\n " % (integers, q, p))

