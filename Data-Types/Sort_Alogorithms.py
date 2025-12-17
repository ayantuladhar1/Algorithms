import random

# Name: Ayan Tuladhar


# Function for insertion sort algorithm.
def sort_for_insert(integers):
    for a in range(1, len(integers)):
        start = integers[a]
        place = a - 1

        while place >= 0 and start < integers[place]:
            integers[place + 1] = integers[place]
            place = place - 1

            integers[place + 1] = start

    return integers


# The following function for quick sort algorithm and quick sort partition was compiled
# form the source referenced below:
# https://www.geeksforgeeks.org/python-program-for-quicksort.
# Function for quick sort partition.
def quick_sort_partition(integers, bottom, top):
    a = (bottom - 1)
    pivot = integers[top]
    for b in range(bottom, top):
        if integers[b] <= pivot:
            a = a + 1
            integers[a], integers[b] = integers[b], integers[a]
    integers[a+1], integers[top] = integers[top], integers[a+1]
    return a+1


# Function for quick sort algorithm.
def quick_sort(integers, bottom, top):
    if len(integers) == 1:
        return integers
    if bottom < top:
        abc = quick_sort_partition(integers, bottom, top)
        quick_sort(integers, bottom, abc-1)
        quick_sort(integers, abc+1, top)
    else:
        return integers


# Test Function for both insertion sort and quick sort.
def test_insertion_sort_and_quick_sort():
    integers = []
    for a in range(0, 20):
        integers.append(random.randint(0, 20))
    print("Random integers from 0 to 20:", integers)
    print("Sorted insertion_sort", sort_for_insert(integers))
    n = len(integers)
    quick_sort(integers, 0, n-1)
    print("Sorted quick_sort:")
    for a in range(0, 20):
        print("%d" % integers[a])


test_insertion_sort_and_quick_sort()
