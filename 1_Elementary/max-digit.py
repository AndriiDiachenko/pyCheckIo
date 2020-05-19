'''
max_digit(0) == 0
max_digit(52) == 5
max_digit(634) == 6
max_digit(1) == 1
max_digit(10000) == 1

Input: A positive int.
Output: An Int (0-9).
'''

def max_digit(numb: int) -> int:
    # max = 0
    # for n in str(numb):
    #     if int(n) > max: max = int(n)
    #
    # return max
    return int(max(str(numb)))

if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1