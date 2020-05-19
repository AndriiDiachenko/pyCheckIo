'''
Check if a given string has all symbols in upper case.
If the string is empty or doesn't have any letter in it - function should return True.

Input: A string.
Output: a boolean.

Example:

is_all_upper('ALL UPPER') == True
is_all_upper('all lower') == False
is_all_upper('mixed UPPER and lower') == False
is_all_upper('') == True
'''

def is_all_upper(txt: str) -> bool:
    return txt.upper() == txt






if __name__ == '__main__':
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    assert is_all_upper(' ') == True
