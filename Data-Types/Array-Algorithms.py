# Name: Ayan Tuladhar


import time
import operator

# The following function was compiled from the powerpoint slide "CSCI 3412 Module7 Quick Sort and Randomized Algorithm")
# The following divide function splits the array into smaller arrays until it ends up with empty array, or that
# has only one element, before recursively sorting the larger arrays.


def divide(just_list, bottom, top):
    a = b = bottom
    x = just_list[top]
    for i in range(bottom, top):
        if just_list[b] <= x:

            just_list[a], just_list[b] = just_list[b], just_list[a]
            b += 1
    just_list[a], just_list[top] = just_list[top], just_list[a]
    return b


# The following function was compiled from the powerpoint slide "CSCI 3412 Module7 Quick Sort and Randomized Algorithm")
# The following KthSmallest function finds the kth smallest value of an "Unsorted Array".
# The function selects a pivot value in array, arranges/partitioning value array about pivot value and recursively
# apply strategy to one of partitions.


def kth_smallest(just_list, bottom, top, k):
    if k > 0 and k <= top - bottom + 1:
        partition = divide(just_list, bottom, top)
        if partition - bottom == k - 1:
            return just_list[partition]
        if partition - bottom > k - 1:
            return kth_smallest(just_list, bottom, partition - 1, k)
        return kth_smallest(just_list, partition + 1, top, k - partition + bottom - 1)
    else:
        return ValueError("K is out of bounds")


# The following function was compiled from the source referenced below:
# https://www.geeksforgeeks.org/python-program-for-quicksort/
# The following quick sort algorithm uses a divide and conquer technique where it picks an elements as pivot and
# partitions the given array around the picked pivot.
# Time complexity: Best case = O(n log n), Worst case = O(n^2) and Average case = O(n^2)


def quick_sort(just_list, bottom, top):
    if len(just_list) == 1:
        return just_list
    if bottom < top:
        partition = divide(just_list, bottom, top)
        quick_sort(just_list, bottom, partition - 1)
        quick_sort(just_list, partition + 1, top)
        return just_list


# The following function was compiled from previous homework assignment "HW-2",
# The following insertion sort algorithm sorts the array one at a time which is much less efficient on a large lists.
# The array elements are compared with each other sequentially and are arranged simultaneously in some particular order.
# Time complexity: Best case = O(n), Worst case = O(n^2) and Average case = O(n^2)


def insertion_sort(just_list, bottom, n):
    for a in range(bottom + 1, n + 1):
        east = just_list[a]
        west = a - 1
        while west >= 0 and east < just_list[west]:
            just_list[west + 1] = just_list[west]
            west = west - 1
        just_list[west + 1] = east


# The following function was compiled fom the source referenced below:
# https://www.geeksforgeeks.org/advanced-quick-sort-hybrid-algorithm/
# The following Hybrid algorithm is the combination of quick sort and insertion sort because quick sort is efficient
# if the size of the input is very large whereas insertion sort is more efficient in case of small arrays but the
# combination of both algorithms helps sort efficiently using both techniques.


def combination_algorithm(just_list, bottom, top, k):
    while bottom < top:
        if top - bottom + 1 < k:
            insertion_sort(just_list, bottom, top)
            break
        else:
            partition = divide(just_list, bottom, top)
            if partition - bottom < top - partition:
                combination_algorithm(just_list, bottom, partition - 1, k)
                bottom = partition + 1
            else:
                combination_algorithm(just_list, partition + 1, top, k)
                top = partition - 1
    return just_list


# The following function was compiled from previous homework assignment "HW-2"
# The following function is to read file for "rand1000000.txt".
# The file "rand1000000.txt contains 1 million integers.


def file_read(file_name):
    just_list = []
    infile = open(file_name)
    for line in infile:
        for a in line.strip().split():
            just_list.append(int(a))
    return just_list


# This is the main function where the Hybrid algorithm is used to find the most optimal k minimizing time
# efficiency of algorithm using 1M data set. The following function collects and displays data performance
# which shows k as the most optimal value.


def main():
    one_million_dataset = "rand1000.txt"
    just_list = []
    print("\n\nTime Efficiency for 1M data set")
    for a in range(1, 5):
        index = file_read(one_million_dataset)
        index2 = len(index)-1
        start = time.time()
        combination_algorithm(index, 0, index2, a)
        end = time.time()
        end_time = end - start
        just_list.append((end_time, a))
        print("The amount of time for: ")
        print(str(end_time), "seconds")
        print("for the value of k: " + (str(a)))
    just_list.sort(key=operator.itemgetter(0))
    print("")
    print("")
    print("Therefore for one million data set the amount of time for:")
    print(str(just_list[0][0]), "seconds")
    print(" for the BEST VALUE of K is " + str(just_list[0][1]))


main()
