import re

def multi_pattern(patterns, phrase):
    for pat in patterns:
        print("searching for pattern {} ".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'aaadsfsdjf......adfads......adeasf.......'
test_patterns = ['ad*']
multi_pattern(test_patterns, test_phrase)
