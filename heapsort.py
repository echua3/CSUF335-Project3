# mergelists_heap.py
# Epiphany Chua
# echua@csu.fullerton.edu
# Spring 2022 CPSC 335 (2)
# Instructor: Dr. Sampson Akwafuo
# April 22, 2022

# Project 3: Array Sorting and Merging
# Algorithm 2: Merging Techniques
import sys

def left(k):
    """
        Function to get left child
        input: 
        k   -   the index of the node
    """
    return 2 * k

def right(k):
    """
        Function to get right child
        input: 
        k   -   the index of the node
    """
    return 2 * k + 1

def min_heapify(L, k):
    l = left(k)     # get the left and right children
    r = right(k)
    # check if smaller than left child
    if l < len(L) and L[l] <= L[k]:
        smallest = l
    else:
        smallest = k
        # check if smaller than right child
    if r < len(L) and L[r] <= L[smallest]:
        smallest = r
    if smallest != k:
        L[k], L[smallest] = L[smallest], L[k]
        min_heapify(L, smallest)


def create_min_heap(L):
    """
        Function that converts a list into a minimum heap.
        The list should begin at index 1.
        In this minimum heap, the value of each internal node is smaller 
        than or equal to the value of its children node. 

        for node at i:
            2i      - left child
            2i + 1  - right child
            i/2     - parent node

        input:
        L - list of comparable values
    """
    n = int(len(L)//2)
    for k in range(n, 0, -1):
        min_heapify(L,k)


def min_heap_merge(all_lists):
    """
        Function that takes a list of sorted-lists and returns
        a sorted list containing all the elements. 
        This algorithm uses a minimum heap.

        input:
        all_lists - list of sorted lists

        return:
        sorted_list - list of sorted values
    """
    # input all the values into an array starting at index 1
    min_heap = [None]
    for l in all_lists:
        print("l:", l)
        min_heap.extend(l)
    
    print("BEFORE MIN HEAP: ", min_heap)
    
    create_min_heap(min_heap)               # create min heap structure
    print("AFTER MIN HEAP: ", min_heap)

    sorted_list = []                        # initialize sorted list
    while len(min_heap) > 1:
        if len(min_heap) <= 2:              # add last element to list
            sorted_list.append(min_heap.pop())
        else:
            sorted_list.append(min_heap[1]) # add smallest value to sortedlist
            min_heap[1] = min_heap.pop()    # swap root and last element
            min_heapify(min_heap, 1)        # heapify

    return sorted_list

def main():
    # check for command line input file argument
    if len(sys.argv) == 2:
        all_lists = []
        with open(sys.argv[1], 'r') as file:
            for line in file:
                current_list = line.rstrip('\n').split(", ")
                all_lists.append(list(map(int, current_list)))
        print("inputted array:", all_lists)
        file.close
        print(mergesort(all_lists))
         
    else: 
        array_1  =[[2, 5, 9, 21],
	       [-1, 0, 2],
	       [-10, 81, 121],
	       [4, 6, 12, 20, 150] ]
        array_2  =[ [10, 17, 18, 21, 29],
	       [-3, 0, 3, 7, 8, 11],
	       [81, 88, 121, 131],
	       [9, 11, 12, 19, 29] ]
        array_3  = [ [-4, -2, 0, 2, 7],
	       [4, 6, 12, 14],
	       [10, 15, 25],
	       [5, 6, 10, 20, 24] ]
        print("Sorted array1: ", min_heap_merge(array_1))
        print("Sorted array2: ", min_heap_merge(array_2))
        print("Sorted array3: ", min_heap_merge(array_3))

if __name__ == "__main__":
    main()