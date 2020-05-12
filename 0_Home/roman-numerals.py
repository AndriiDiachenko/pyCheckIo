'''
you should return a roman numeral using the specified integer value ranging from 1 to 3999.

Input: A number as an integer.
Output: The Roman numeral as a string.

Example:
checkio(6) == 'VI'
checkio(76) == 'LXXVI'
checkio(13) == 'XIII'
checkio(44) == 'XLIV'
checkio(3999) == 'MMMCMXCIX'
'''

def checkio(digit: int) -> str:

    text = ''
    rom = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    for key in rom:
        if digit//key >0:
            text += rom[key] * (digit//key)
            digit -=key * (digit//key)

    return text

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'