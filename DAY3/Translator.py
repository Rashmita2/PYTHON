#convert the vowel to r from the word
def tran_func(phrase):
    tran_func = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            tran_func = tran_func + "r"
        else:
            tran_func = tran_func + letter
    return tran_func

print(tran_func("University"))