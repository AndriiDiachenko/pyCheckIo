'''
You are given a set of square coordinates where we have placed white pawns.
You should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.

Output: The number of safe pawns as a integer.

Example:

safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
'''

def safe_pawns(pawns: set) -> int:
    pawns_cordinates = tuple((ord(i[0]) - 96, int(i[1])) for i in pawns)
    print(pawns_cordinates)



safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})