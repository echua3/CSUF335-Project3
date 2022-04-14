# mergelists.py
# Epiphany Chua
# echua@csu.fullerton.edu
# Spring 2022 CPSC 335 (2)
# Instructor: Dr. Sampson Akwafuo
# April 22, 2022

# Project 3: Array Sorting and Merging
# Algorithm 2: Merging Techniques

import sys

def mergesort(all_lists):
    """
        Function that takes a list of sorted-lists and returns
        a sorted list containing all the elements. 
        Important: This function assumes all lists are sorted.

        input:
        all_lists - list of sorted lists

        return:
        sorted_list - list of sorted values
    """
    sorted_list = []
    # iterates until all_lists is empty
    while all_lists:
        # initialize index of list, contains smallest value in the entire list
        smallest_i = 0 
        for i in range(1, len(all_lists)):
            if all_lists[i][0] < all_lists[smallest_i][0]:
                smallest_i = i
        # remove the smallest value from all_lists and append to list
        smallest = all_lists[smallest_i].pop(0)
        sorted_list.append(smallest)
        # removes empty list from all_lists
        if (len(all_lists[smallest_i]) == 0):
            all_lists.pop(smallest_i)
        
    return sorted_list

def main():
    # check for command line input file
    if len(sys.argv) == 1:
        array1 = []
        with open(sys.argv[1], 'r') as file:
            for line in file:
                array1.append(line)
        print(array1)
        file.close
    else: 
        all_lists = [[0], [1,2], [4]]
        # print("all_lists:", all_lists)
        # all_lists[0].pop(0)
        # print("all_lists:", all_lists)
        # if(len(all_lists[0]) == 0):
        #     all_lists.pop(0)
        # print("all_lists:", all_lists)
        all_lists1 = [[0], [1,2], [4], [1, 2, 3]]
        print("all_lists: ", mergesort(all_lists))
        print("all_lists1: ", mergesort(all_lists1))

if __name__ == "__main__":
    main()