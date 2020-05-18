'''
You are given a set of square coordinates where we have placed white pawns.
You should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.

Output: The number of safe pawns as a integer.

Example:

safe_pawns({"a1", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
'''

def safe_pawns(pawns: set) -> int:

    safe_pown = 0
    for pawn in pawns:
        if chr(ord(pawn[0]) - 1) + str(int(pawn[1]) - 1) in pawns or chr(ord(pawn[0]) + 1) + str(
            int(pawn[1]) - 1) in pawns:
            safe_pown += 1
    return safe_pown





print(safe_pawns({"a4", "d4", "f4", "c3", "e3", "g5", "d2"}))