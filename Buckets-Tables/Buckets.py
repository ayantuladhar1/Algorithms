# Name: Ayan Tuladhar


from random import seed
from random import randint
import math


class SortFunction:

    # The following function finds minimum and maximum values, initialize buckets, sorts the bucket and place back into
    # input array.

    def sort_for_bucket(self, index):
        if len(index) == 0:
            print('No elements found!')
        size_of_bucket = 100
        bottom = index[0]
        top = index[0]
        for a in range(0, len(index)):
            if index[a] < bottom:
                bottom = index[a]
            elif index[a] > top:
                top = index[a]
        count_for_bucket = math.floor((top - bottom) / size_of_bucket) + 1
        buck_list = []
        for a in range(0, count_for_bucket):
            buck_list.append([])
        for a in range(0, len(index)):
            buck_list[math.floor((index[a] - bottom) / size_of_bucket)].append(index[a])
        after_sorted = []
        for a in range(0, len(buck_list)):
            self.sort_for_insertion(buck_list[a])
            for b in range(0, len(buck_list[a])):
                after_sorted.append(buck_list[a][b])
        return after_sorted

    # The following insertion sort function is used in bucket sort.

    def sort_for_insertion(self, elements):
        for a in range(1, len(elements)):
            top = elements[a]
            b = a - 1
            while b >= 0 and elements[b] > top:
                elements[b + 1] = elements[b]
                b -= 1
            elements[b + 1] = top
        return elements

    # The following function read and write the file with 1000000 random integers from the path
    # "C:\Users\Ayan_\PycharmProjects\merge\rand1000000.txt"

    def __init__(self):

        # The following function finds the file 'rand1000000.txt' in the path directory.

        txt_file = 'C:\\Users\\Ayan_\\PycharmProjects\\merge\\rand1000000.txt'

        # The following 'r+' command reads and writes the rand1000000.txt file before sorting the process.
        # Please note, if there is no 'rand1000000.txt file to read in the path, it will print error message.

        main_file = open(txt_file, 'r+')
        print('File Opening in progress')

        # The following seed function generates random integers - if it can't find the file to read.

        seed(1)
        for a in range(1000000):
            one_million = randint(1, 1000000)
            print(one_million, file=main_file)

        # The following function distributes into 100 sublist containing 10000 integers each for sorting.

        rad_buck = [[0 for a in range(0, 10000)] for b in range(0, 100)]
        main_file.close()

        # The following function reads the file rand1000000.txt and creates 100 files of size 10000 integers each-
        # and then split files which will be name split_1.txt up to split_100.txt.

        splits = open('C:\\Users\\Ayan_\\PycharmProjects\\merge\\split_', 'w')
        with open(txt_file) as in_file:
            column = 0
            row = 0
            for line in in_file:
                rad_buck[row][column] = int(line)
                print(line, file=splits, end='')
                column = column + 1
                if column % 10000 == 0:
                    splits.close()
                    column = 0
                    row = row + 1
                    splits = open('C:\\Users\\Ayan_\\PycharmProjects\\merge\\split_' + str(row) + '.txt', 'w')
        splits.close()

        # The following function sorts the 50 list using radix sort with counting sort as underlying-
        # sort for each digit.

        for a in range(0, 50):
            rad_buck[a] = self.radix_sort(rad_buck[a])

        # The following function sorts the 50 list using bucket sort.

        for a in range(50, 100):
            rad_buck[a] = self.sort_for_bucket(rad_buck[a])
        result = rad_buck[0]

        # The following function merges 100 sorted sub-lists into one sorted list.

        for a in range(1, 100):
            result = self.final_merge(result, rad_buck[a])

        # The following function then writes the output to merged file 'sorted.txt'.

        splits = open('C:\\Users\\Ayan_\\PycharmProjects\\merge\\sorted.txt', 'w')
        for a in range(0, 100):
            for b in range(0, 10000):
                print(rad_buck[a][b], file=splits)
        splits.close()

    # The following count sort function initializes array as 0 and store count of occurrences in count [].

    def sort_for_count(self, elements, occ):
        x = len(elements)
        output = [0] * x
        count = [0] * 10
        for a in range(0, x):
            index = (elements[a] / occ)
            count[(int(index) % 10)] += 1
        for a in range(1, 10):
            count[a] += count[a - 1]
        a = x - 1
        while a >= 0:
            index = (elements[a] / occ)
            output[count[int(index % 10)] - 1] = elements[a]
            count[int(index % 10)] -= 1
            a -= 1
        a = 0
        for a in range(0, len(elements)):
            elements[a] = output[a]
        return elements

    # The following radix sort function sorts upto 6 digit integers.

    def radix_sort(self, elements):
        occ1 = 1
        for n in range(6):
            elements = self.sort_for_count(elements, occ1)
            occ1 = occ1 * 10
        return elements

    # The following merge function merges arrays which traverse both ways, checks if the current element of first array
    # is smaller than same for second array, then stores first array element and increment first array index.

    def final_merge(self, elements1, elements2):
        x1 = len(elements1)
        x2 = len(elements2)
        elements3 = [0] * (x1 + x2)
        a, b, c = 0, 0, 0
        while a < x1 and b < x2:
            if elements1[a] < elements2[b]:
                elements3[c] = elements1[a]
                c = c + 1
                a = a + 1
            else:
                elements3[c] = elements2[b]
                c = c + 1
                b = b + 1
        while a < x1:
            elements3[c] = elements1[a]
            c = c + 1
            a = a + 1
        while b < x2:
            elements3[c] = elements2[b]
            c = c + 1
            b = b + 1
        return elements3


def main():

    print("This program reads the 1M integers and splits into 100 lists with 10000 integers.")
    print("Radix sorts 50 sub-lists with counting sort.")
    print("Bucket sorts remaining 50 sub-lists.")
    print("Finally merges the 100 sorted sub-lists into one sorted list")
    print("If error occurs please check the path and make sure there are no errors.")
    print("An example of path = C:\\Users\\Ayan_\\PycharmProjects\\merge\\")
    print("where all the sorted and splitted txt files are stored under 'Merge' folder.")
    print("The sorting has began")
    SortFunction()
    print('The sorting has completed. Please check your path folder for sorted txt files.')


main()
