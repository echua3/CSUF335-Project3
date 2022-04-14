# CSUF335-Project3
## Project 3: Array Sorting and Merging

## Spring 2022 CPSC 335 - Algorithm Engineering

### Epiphany Chua echua@csu.fullerton.edu

[Github Repo link](https://github.com/echua3/CSUF335-Project3/tree/main "CPSC 335 Project 3 git Repo")

Includes **Algorithm 1: Finding Target Substrings** and **Algorithm 2: Merging Techniques**
### Algorithm 1: Finding Target Substrings
The script **substrings.py** accepts a txt document as input and prints the
indices of the target words ascending order of their appearances and print the
words, according to the resulting of appearance. 

The txt document must be in the format depicted below.
```
# test.txt
str2str1str3etc
str1, str2, str3, etc
```
running `python3 text.txt`
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