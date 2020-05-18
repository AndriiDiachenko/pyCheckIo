'''
Your mission here is to create a function that gets a tuple and
returns a tuple with 3 elements -
the first,
third and
second element from the last for the given array.
'''

def easy_unpack(items: tuple) -> tuple:
    return (items[0], items[2], items[-2])

