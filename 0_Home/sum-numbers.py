'''
In a given text you need to sum the numbers. Only separated numbers should be counted. If a number is part of a word it shouldn't be counted.
The text consists from numbers, spaces and english letters

Input: A string.
Output: An int.

sum_numbers('hi') == 0
sum_numbers('who is 1st here') == 0
sum_numbers('my numbers is 2') == 2
sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
sum_numbers('5 plus 6 is') == 11
sum_numbers('') == 0
'''

# My stupid way
def sum_numbers(txt):
    sm = 0
    for w in txt.split():
        try:
            sm +=int(w)
        except ValueError:
            continue

    return sm

# Quick way:
def sum_numbers_two(txt):
    return sum(int(w) for w in txt.split() if w.isdigit())



