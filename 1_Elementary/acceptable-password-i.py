'''
In this mission you need to create a password verification function.
Those are the verification conditions:

the length should be bigger than 6.
Input: A string.

Output: A bool.

Example:

is_acceptable_password('short') == False
is_acceptable_password('muchlonger') == True
'''

def is_acceptable_password(input: str) -> bool:
    return True if len(input) > 6 else False

if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")