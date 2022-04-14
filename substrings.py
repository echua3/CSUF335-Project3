# substrings.py
# Epiphany Chua
# echua@csu.fullerton.edu
# Spring 2022 CPSC 335 (2)
# Instructor: Dr. Sampson Akwafuo
# April 22, 2022

# Project 3: Array Sorting and Merging
# Algorithm 1: Finding Target Substrings

import sys


def find_targets(array1, array2):
    """
        Function that takes two lists and finds the indices of the values of
        array2 in array1's string. A list with the indices in ascending 
        order of their appearance in array1 and a list of the words in
        the order they appear are returned.

        input:
        array1  - list of length 1 with one string at array1[0]
        array2  - list of multiple strings found in array1

        return:
        order   - list of indices in ascending order of their appearance in 
                array1
        targets - list of the words in the order they appear
    """
    # initialize dictionary to store the results
    result = {}

    # total nested for-loop complexity = O(n^2):
    # iterate through every target word in the second array
    # O(n) linear time efficiency
    for word in array2:
        # iterate from 0 to the len(array1) - len(word) + 1
        # (ensures that the word can be formed)
        # O(n) linear time efficiency
        for index in range(len(array1[0]) - len(word) + 1):
            # current string = [index, index + wordlength]
            # check if the current string matches target word 
            if array1[0][index:index + len(word)] == word:
                # add word:index to dictionary
                result.update({word:index})
                break
    
    # sort dictionary by index values to list in ascending order
    # python's sort function has O(nlogn) efficiency
    result = dict(sorted(result.items(), key=lambda item: item[1]))

    # returns tuple(list of indices, list of words)
    # O(n + n) = O(2n) = O(n) linear time efficiency 
    return list(result.values()), list(result.keys())


def main():

    # check for command line input files
    if len(sys.argv) == 2:
        array1 = []
        array2 = []
        file = open(sys.argv[1], 'r') 
        array1.append(file.readline().rstrip('\n'))
        array2 = file.readline().split(", ")
        file.close
        # execute find_targets algorithm
        a1, b1 = find_targets(array1, array2)
        print("{a}\n{b}".format(a = a1, b = b1))

    # no command line argument
    # the script initializes the three given input arrays
    else: 
        
        # 3 input arrays from in3A-1
        array1a = ['sanoaklandrialtofullertonmarcolongchinocoronamodestoclovissimithousand']
        array1b = ['oakland', 'modesto', 'clovis', 'corona']

        array2a = ['polmonafremontrialtofullertonmarcolongfresnochinoclovissimisalinas']
        array2b = ['fullerton', 'chino', 'fremont', 'fresno']

        array3a = ['torranceoaklandrialtomarcooxnardchinofresnoirvineclovissimiorange']
        array3b = ['oxnard', 'irvine', 'orange', 'marco']

        a1, b1 = find_targets(array1a, array1b)
        a2, b2 = find_targets(array2a, array2b)
        a3, b3 = find_targets(array3a, array3b)
        print("{a}\n{b}".format(a = a1, b = b1))
        print("{a}\n{b}".format(a = a2, b = b2))
        print("{a}\n{b}".format(a = a3, b = b3))
        

if __name__ == "__main__":
    main()