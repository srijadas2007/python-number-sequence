# Number Sequence Digit Position Finder

## Description
Python program that shows digit positions in number sequences.

## Usage
1. Run: `python number_sequence.py`
2. Enter a number
3. See digit positions

## Example
Input: 12
Output: 
1th digit is 1
2th digit is 2
...
12th digit is 1

## Code
```python
n = int(input("Enter a number: "))
result = ""
for i in range(1, n + 1):
    result += str(i)
for index, digit in enumerate(result, start=1):
    print(f"{index}th digit is {digit}")