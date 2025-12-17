```python
#%%

# Name: Ayan Tuladhar


3.1  Write down general description of loop invariant technique  in your own words as proof technique of correctness.
(2 points)

Generally, in iteration of a loop, before and after each iteration of a loop, loop invariant acts as a statement
which is true about program variable. In a simple program, invariant loop consists of three different properties
which are Initializing the loop, Maintaining the loop, and Terminating the loop.

For example,

a, b = 0, 0
Initializing the loop:

while True or (True statement)
while b <= j(where j is an integer)
Maintaining the loop:

    a = a + b
    b = b + 1
Terminating the loop:

    return a

There are different examples for loop variant proof like Merge Sort, Bubble Sort, Insertion Sort etc.
In this case we use the Merge Sort function.

For example,

merge_sort(L, bottom, center, top)
east = L[bottom: center]
west = L[center + 1, Top]
a, b = 1, 1
    for i = bottom to top:
        if east[a] < west[b]
            L[i] = east[a]
            a = a + 1
        else:
            L[i] = west[b]
            b = b + 1

Invariant:

In this case, array starts at L[i] where i represents the length when the loop iterates.

Initializing the loop:

As L[i] where the array starts, east and west are sorted as i – bottom = 0.
Maintaining the loop:
For east, the value of L[i] is smallest
For west, the value of west[b] is smallest
east and west are sorted

Terminating the loop:

During the last iteration L[bottom: top] is sorted as i – bottom(bottom.top + 1) which also sorts L[bottom]
where I represents the length.i – bottom = (top + 1) – bottom = top – bottom + 1 So, L[bottom: top] is sorted.

3.2 Identify the loop invariant of the loop in your merge() function (3 points)

From part 2
At the start of each loop iteration the array starts at integers[] where we have east_side which focuses on
left side of the list and west_side which focuses on right side of the list to begin sorting.
finds the mid of the array
center = len(integers)//2
east_side = integers[:center]
west_side = integers[center:]
the array elements inside the list are divided and sorted into two halves with the following
sort_for_merge(east_side)
sort_for_merge(west_side)

3.3  Describe initialization step (0 points)

As integers[] where array starts, east_side and west_side are sorted. It will continue looping if it satisfies
loop variant.

3.4  Describe maintenance  step (4 points)

The merge sort algorithm uses the following techniques as follows:
1 - Divide(divides into sub arrays)
2 - Conquer(recursive process sub arrays until every elements are solved)
3 - Combine(after all the elements are solved it then combines to produce a solution to the original problem)

Merge sort algorithm uses O(n(logn)) application to sort the problem. Generally, in the maintenance step the
rule of thumb is "if the invariant is true before an iteration of the loop then it should also be true after
the iteration", when sort proceeds the program checks if the left number is smaller than right number and
moves on for every elements in the list.
Here, from the previous iteration the elements on east_side amd west_side are sorted.

if east_side[east_left] < west_side[west_right]
    integers[east_west] = east_side[east_left]
    east_left = east_left + 1
else:
    integers[east_west] = west_side[west_right]
    west_right = west_right + 1
    east_west = east_west + 1

3.5  Describe Termination step (1 point)

In termination process, the invariant states that array is sorted when the loop terminates. In this case, the loop
invariant is true and elements inside the list is sorted when while loop terminates.


#%%
```
