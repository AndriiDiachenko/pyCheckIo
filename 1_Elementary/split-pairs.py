'''
Split the string into pairs of two characters.
If the string contains an odd number of characters,
 then the missing second character of the final pair should be replaced with an underscore ('_').

Input: A string.
Output: An iterable of strings.

Example:
split_pairs('abcd') == ['ab', 'cd']
split_pairs('abc') == ['ab', 'c_']
'''

def split_pairs(text: str) -> list:

    if len(text) % 2 !=0: text+="_"
    return [text[i: i+2] for i in range(0, len(text), 2)]

