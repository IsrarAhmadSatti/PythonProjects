
def Vowel_Eater(user_word):
    word_without_vowels = ""
    user_word = user_word.upper()
    vowel = ["A","E","I","O","U"]
    vowels=""

    for letter in user_word:
        if letter in vowel:
            vowels += letter
            continue
        else:
            word_without_vowels += letter
    print("Here is the string after eating vowels\t", word_without_vowels)
    print("These are the vowels eaten\t", vowels)

user_word=str(input('enter any string:  '))
Vowel_Eater(user_word)
