'''
You are given an array of integers. You should find the sum of the integers with even indexes (0th, 2nd, 4th...).
Then multiply this summed number and the final element of the array together.
Don't forget that the first element has an index of 0.
For an empty array, the result will always be 0 (zero).

Input: A list of integers.
Output: The number as an integer.

checkio([0, 1, 2, 3, 4, 5]) == 30
checkio([1, 3, 5]) == 30
checkio([6]) == 36
checkio([]) == 0
'''

def evenLast(lst):
    return (sum(numb for numb in lst[::2]) * lst[-1]) if len(lst) > 0 else 0

