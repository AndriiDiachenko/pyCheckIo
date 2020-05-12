'''
In this mission you should check if all elements in the given list are equal.

Input: List.
Output: Bool.
Example:
all_the_same([1, 1, 1]) == True
all_the_same([1, 2, 1]) == False
all_the_same(['a', 'a', 'a']) == True
all_the_same([]) == True
'''


def all_the_same(elements: list) -> bool:
    for e in elements:
        if e != elements[0]:
            return False
    return True
