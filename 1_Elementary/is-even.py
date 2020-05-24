'''
Check is the given number is even or not.
Your function shoudl return True if the number is even, andFalse if the number is odd.

both given ints should be between -1000 and 1000
'''

def is_even(numb: int) -> bool:
    return True if abs(numb) % 2 == 0 else False


print(is_even(-200))