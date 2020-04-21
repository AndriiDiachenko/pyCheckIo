'''
You are given a string with words and numbers separated by whitespaces (one space).
The words contains only letters. You should check if the string contains three words in succession.
For example, the string "start 5 one two three 7 end" contains three words in succession.

Input: A string with words.
Output: The answer as a boolean.

Example:
checkio("Hello World hello") == True
checkio("He is 123 man") == False
checkio("1 2 3 4") == False
checkio("bla bla bla bla") == True
checkio("Hi") == False
'''

# v1
def threeWordsCheck(text: str):
    counter = 0
    for w in text.split():
        if w.isalpha():
            counter +=1
            if counter == 3:
                break
        else:
            counter = 0
    return True if counter == 3 else False

# v2

def threew(text: str):
    counter = 0
    for w in text.split():
        counter +=1 * w.isalpha()
        if counter == 3:
            return True
    else:
        return False
