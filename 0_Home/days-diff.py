'''
You are given two dates as an array with three numbers - a year, month and day.
For example: 19 April 1982 will be (1982, 4, 19).
You should find the difference in days between the given dates.
For example between today and tomorrow = 1 day.
The difference will always be either a positive number or zero, so don't forget about the absolute value.

Input: Two dates as tuples of integers.
Output: The difference between the dates in days as an integer.

Example:
days_diff((1982, 4, 19), (1982, 4, 22)) == 3
days_diff((2014, 1, 1), (2014, 8, 27)) == 238
'''

from datetime import date

def days_diff(a, b):
    d1, d2 = date(*a), date(*b)
    return abs(d1-d2).days


assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
assert days_diff((1, 1, 1), (9999, 12, 31)) == 3652058