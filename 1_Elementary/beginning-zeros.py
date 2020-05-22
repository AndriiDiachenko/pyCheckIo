'''
You have a string that consist only of digits.
You need to find how many zero digits ("0") are at the beginning of the given string.

Input: A string, that consist of digits.
Output: An Int.

Example:
beginning_zeros('100') == 0
beginning_zeros('001') == 2
beginning_zeros('100100') == 0
beginning_zeros('001001') == 2
beginning_zeros('012345679') == 1
beginning_zeros('0000') == 4
'''

import time

def timer(func):
    st = time.process_time()
    def wrapper(*args, **kwargs):
        return func(*args,**kwargs)
    et = time.process_time()
    print(et - st)
    return wrapper


@timer
def beginning_zeros(numbs: str) -> int:
    zeros = 0
    for n in numbs:
        if int(n) == 0: zeros +=1
        else: return zeros
    return zeros



beginning_zeros('00001000')
