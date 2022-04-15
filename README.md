# CSUF335-Project3
## Project 3: Array Sorting and Merging

## Spring 2022 CPSC 335 - Algorithm Engineering

### Epiphany Chua echua@csu.fullerton.edu

[Github Repo link](https://github.com/echua3/CSUF335-Project3/tree/main "CPSC 335 Project 3 git Repo")

Includes **Algorithm 1: Finding Target Substrings** and **Algorithm 2: Merging Techniques**
### Algorithm 1: Finding Target Substrings
The script **substrings.py** accepts a txt document as input and prints the
indices of the target words ascending order of their appearances and prints the
words, according to the resulting of appearance. 

The txt document must be in the format depicted below.
```
# test.txt
str2str1str3etc
str1, str2, str3, etc
```
running `python3 substrings.py test.txt`
```
[0, 4, 8, 12]
['str2', 'str1', 'str3', 'etc']
```


If no document is passed, running `python3 substrings.py` will print the 
resulting lists from the given input arrays found in in3A-1.docx. These sample
inputs can also be separately tested using the files in3A-1.txt, in3A-2.txt,
and in3A-3.txt.
```
python3 substrings.py in3A-1.txt
python3 substrings.py in3A-2.txt
python3 substrings.py in3A-3.txt
```

will return
```
[3, 39, 45, 52]
['oakland', 'corona', 'modesto', 'clovis']

[7, 20, 38, 44]
['fremont', 'fullerton', 'fresno', 'chino']

[21, 26, 43, 59]
['marco', 'oxnard', 'irvine', 'orange']
```
### Algorithm 2: Merging Techniques
The scripts **mergelists.py** and **heapsort.py** accept a txt document as input and 
returns and prints the given list of lists as a 1 dimensional sorted list.
The txt document must be in the format depicted below.
```
# test2.txt
0, 1, 3
2, 9, 15, 17
-1, 2
```
running `python3 mergelists.py test2.txt`
```
[-1, 0, 1, 2, 2, 3, 9, 15, 17]
```
If no document is passed, running `python3 mergelists.py` will print the 
resulting lists from the given input arrays found in in3B.docx. These sample
inputs can also be separately tested using the files in3B-1.txt, in3B-2.txt,
and in3B-3.txt.
```
python3 substrings.py in3A-1.txt
python3 substrings.py in3A-2.txt
python3 substrings.py in3A-3.txt
```

will return
```
[-10, -1, 0, 2, 2, 4, 5, 6, 9, 12, 20, 21, 81, 121, 150]

[-3, 0, 3, 7, 8, 9, 10, 11, 11, 12, 17, 18, 19, 21, 29, 29, 81, 88, 121, 131]

[-4, -2, 0, 2, 4, 5, 6, 6, 7, 10, 10, 12, 14, 15, 20, 24, 25]
```

Similarily, 
running `python3 heapsort.py test2.txt`
```
[-1, 0, 1, 2, 2, 3, 9, 15, 17]
```
If no document is passed, running `python3 heapsort.py` will print the 
resulting lists from the given input arrays found in in3B.docx. These sample
inputs can also be separately tested using the files in3B-1.txt, in3B-2.txt,
and in3B-3.txt.
```
python3 substrings.py in3A-1.txt
python3 substrings.py in3A-2.txt
python3 substrings.py in3A-3.txt
```

will return
```
[-10, -1, 0, 2, 2, 4, 5, 6, 9, 12, 20, 21, 81, 121, 150]

[-3, 0, 3, 7, 8, 9, 10, 11, 11, 12, 17, 18, 19, 21, 29, 29, 81, 88, 121, 131]

[-4, -2, 0, 2, 4, 5, 6, 6, 7, 10, 10, 12, 14, 15, 20, 24, 25]
```

### Project 3
The script **project3.py** accepts two txt documents as input. The first file
uses **substrings.py** to print the indices of the target words ascending order
of their appearances and prints the words, according to the resulting of 
appearance. The second text file uses **mergelists.py** to print the given list
of lists as a 1 dimensional sorted list.

file1.txt and file2.txt must match the descriptions described earlier.