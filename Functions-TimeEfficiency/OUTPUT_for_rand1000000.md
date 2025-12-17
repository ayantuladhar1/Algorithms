```python
#!/usr/bin/python3
# Name: Ayan Tuladhar
# Student Id: 109974948
import time
# Function to read an input file as txt file.


def file_input(integers):
    start_list = []
    while True:
        txt = input("Enter file name such as rand1000.txt or rand1000000.txt:")
        file = open(txt, "r")
        for line in file:
            for i in line.strip().split():
                integers.append(int(i))
        file.close()
        return start_list

# The following code was used to compile and create a insertion sort function which is referenced below:
# https://github.com/tylrdvs277/ComparisonSorting/blob/master/comparison_sort.py
# Function to create insertion sort method to sort the integers from 1 to ...n.
# The sorted array is built on at a time where the elements are compared and then arranged in a particular order.


def sort_for_insert(integers):
    # Count starts at 0
    compare = 0
    for a in range(1, len(integers)):
        start = integers[a]
        place = a - 1
        compare = compare + 1
        while place >= 0 and start < integers[place]:
            integers[place + 1] = integers[place]
            place = place - 1
            compare = compare + 1
            integers[place + 1] = start
    print("The following displays the total number of comparison for insertion sort program:")
    print(compare)
    print("")

# The following code was used to compile and create a merge sort function which is referenced below:
# https://stackoverflow.com/questions/42608630/how-to-add-a-comparison-counter-for-merge-sort-in-python
# Function to create merge sort method to sort the integers from 1 to ...n.
# The sorted array splits the elements into two groups and recursively sort each groups.
# Uses Run time = O(nlogn)


def sort_for_merge(integers):
    compare = 0
    if len(integers) > 1:
        center = len(integers) // 2
        east_side = integers[:center]
        west_side = integers[center:]
        east_side_1, west_side_1 = sort_for_merge(east_side), sort_for_merge(west_side)
        compare += east_side_1 + west_side_1
        east_left, west_right, east_west = 0, 0, 0
        while east_left < len(east_side) and west_right < len(west_side):
            compare = compare + 1
            if east_side[east_left] < west_side[west_right]:
                integers[east_west] = east_side[east_left]
                east_left = east_left + 1
            else:
                integers[east_west] = west_side[west_right]
                west_right = west_right + 1
            east_west += 1
        while east_left < len(east_side):
            integers[east_west] = east_side[east_left]
            east_left = east_left + 1
            east_west = east_west + 1
            compare = compare + 1
        while west_right < len(west_side):
            integers[east_west] = west_side[west_right]
            west_right = west_right + 1
            east_west = east_west + 1
            compare = compare + 1
    return compare

# The following code was used from HW1 for time efficiency function for both insertion and merge sort function.
# Function to display and compare time efficiency for both merge and insertion sort function


def main():
    integers = []
    file_input(integers)
    begin = time.time()
    sort_for_insert(integers)
    end = time.time()
    print("The following displays the start time of insertion sort program:")
    print(begin)
    print("")
    print("The following displays the end time of insertion sort program:")
    print(end)
    print("")
    print("The following displays the execution time for insertion sort program:")
    print(end - begin)
    print("")
    begin = time.time()
    sort_for_merge(integers)
    end = time.time()
    compare1 = sort_for_merge(integers)
    print("The following displays the total number of comparison for merge sort program:")
    print(compare1)
    print("")
    print("The following displays the start time of merge sort program:")
    print(begin)
    print("")
    print("The following displays the end time of merge sort program:")
    print(end)
    print("")
    print("The following displays the execution time of merge sort program:")
    print(end - begin)
    print("")


main()

```

    Enter file name such as rand1000.txt or rand1000000.txt:rand1000000.txt
    The following displays the total number of comparison for insertion sort program:
    249926868108
    
    The following displays the start time of insertion sort program:
    1613966552.573458
    
    The following displays the end time of insertion sort program:
    1614033561.317532
    
    The following displays the execution time for insertion sort program:
    67008.74407410622
    
    The following displays the total number of comparison for merge sort program:
    19951424
    
    The following displays the start time of merge sort program:
    1614033561.317532
    
    The following displays the end time of merge sort program:
    1614033566.60215
    
    The following displays the execution time of merge sort program:
    5.284617900848389
    
    


```python

```
