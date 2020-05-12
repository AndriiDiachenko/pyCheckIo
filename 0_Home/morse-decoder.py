'''
Your task is to decrypt the secret message using the Morse code.
The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
If the decrypted text starts with a letter then you'll have to print this letter in uppercase.

morse_decoder("... --- -- .   - . -..- -") == "Some text"
morse_decoder("..--- ----- .---- ---..") == "2018"
morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
'''

def morse_decoder(message: str):
    # Original Morse codes dict
    morse_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

    # Reversed Morse dict where values use as keys
    morse_ch_dict = dict((code, let.lower()) for let, code in morse_dict.items())

    # Each world has 3 spaces distance
    words = message.split("   ")
    trans = ""

    # for w in words:
    #     # Each letter has a 1 space distance
    #     chars = w.split(" ")
    #     for ch in chars:
    #         trans += morse_ch_dict[ch]
    #     trans += " "
    #
    # return trans.capitalize().rstrip()

    # return " ".join(
    #     ["".join([morse_ch_dict[mc] for mc in words.split()]) for words in message.split("  ")]
    # ).capitalize()

print(morse_decoder("... --- -- .   - . -..- -"))

