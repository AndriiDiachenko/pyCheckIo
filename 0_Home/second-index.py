'''
You are given two strings and you have to find an index of the second occurrence of the second string in the first one.

Input: Two strings.
Output: Int or None

Example:

second_index("sims", "s") == 3
second_index("find the river", "e") == 12
second_index("hi", " ") is None
'''




def second_index(text: str, symbol: str):
    try:
        return text.index(symbol, text.index(symbol) + 1)
    except ValueError:
        return None


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')