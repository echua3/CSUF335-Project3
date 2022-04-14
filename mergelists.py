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
        Important! This function assumes all lists are sorted.

        input:
        all_lists - list of sorted lists

        return:
        sorted_list - list of sorted values
    """
    # check for valid input
    if len(all_lists) == 0:
        return all_lists
    elif len(all_lists) == 1:
        return all_lists[0]

    sorted_list = []    # initialize sorted list
    # iterates while all_lists is not empty
    while all_lists:
        # removes first list in all_lists if it is empty
        if len(all_lists[0]) < 1:
            all_lists.pop(0)
        elif len(all_lists) == 1:
            # appends the rest of the last list and exits while loop
            sorted_list.extend(all_lists[0])
            break
        else:
            # initialize list that contains smallest value
            smallest = all_lists[0] 
            for l in all_lists[1:]:
                if (len(l) > 0) and l[0] < smallest[0]:
                    smallest = l

            # remove the smallest value from all_lists and append to list
            sorted_list.append(smallest[0])
            smallest.pop(0)
            
            # removes empty list from all_lists
            if (len(smallest) == 0):
                all_lists.remove(smallest)
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
        print(mergesort(array_1))
        print(mergesort(array_2))
        print(mergesort(array_3))

if __name__ == "__main__":
    main()