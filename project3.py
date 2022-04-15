# project3.py
# Epiphany Chua
# echua@csu.fullerton.edu
# Spring 2022 CPSC 335 (2)
# Instructor: Dr. Sampson Akwafuo
# April 22, 2022

# Project 3: Array Sorting and Merging
# Algorithm 2: Merging Techniques
import os
import substrings
import mergelists
import heapsort
import sys


def main():
    """
        function  used to run substrings.py, mergelists.py and heapsort.py
        at the same time.
    """
    # check for command line input file argument
    if len(sys.argv) == 3:
        # algorithm 1:
        array1 = []
        array2 = []
        file = open(sys.argv[1], 'r') 
        array1.append(file.readline().rstrip('\n'))
        array2 = file.readline().split(", ")
        file.close
        a1, b1 = substrings.find_targets(array1, array2)
        print("{a}\n{b}".format(a = a1, b = b1))

        # Algorithm 2
        all_lists = []
        with open(sys.argv[2], 'r') as file:
            for line in file:
                current_list = line.rstrip('\n').split(", ")
                all_lists.append(list(map(int, current_list)))
        print("Input:", all_lists)
        file.close
        print(heapsort.min_heap_merge(all_lists))
         
    else: 
        # Run three python files' main function with the sample input
        print ("substrings.py:")
        substrings.main()
        print ("mergelists.py:")
        mergelists.main()
        print ("heapsort.py:")
        heapsort.main()

if __name__ == "__main__":
    main()