"""
Cette fonction traduit du texte de l'anglais en Pig Latin.
La traduction utilise 4 règles qui regardent les voyelles et les consonnes au début de chaque mot.
Rappel :
- voyelles : a, e, i, o, u
- consonnes : les 21 autres lettres de l'alphabet
Règle 1 : si un mot commence avec une voyelle ou avec "xr" ou "yt", ajoute "ay" à la fin du mot
Règle 2 : si un mot commence avec une ou plusieurs consonnes, déplace ces consonnes à la fin du mot et ajoute "ay" à la fin.
Règle 3 : si un mot commence avec aucune ou plusieurs consonnes suivies de "qu", déplace ces consonnes à la fin du mot et ajoute "ay" à la fin.
Règle 4 : si un mot commence avec une ou plusieurs consonnes suivies de "y", déplace les consonnes précédant le "y" à la fin du mot et ajoute "ay" à la fin.
"""



def translate_word(word):
    """
    :param word: string - le word à traduire
    :result: string - le word traduit
    """
    vowels = ["a", "e", "i", "o", "u"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x" ,"y" ,"z"]
    pig_latin_adding = "ay"
    if len(word) > 2:
        print(len(word))
    # si un mot commence avec une voyelle ou avec "xr" ou "yt", ajoute "ay" à la fin du mot
        # if word[0] in vowels or word[0:2] == "xr" or word[0:2] == "yt":
        #     return word + pig_latin_adding
        if word[0] in vowels or word.startswith("xr") or word.startswith("yt"):
            print(word + pig_latin_adding)
            return word + pig_latin_adding
    # si un mot commence avec une ou plusieurs consonnes suivies de "y", déplace les consonnes précédant le "y" à la fin du mot et ajoute "ay" à la fin

        # if word[0] in consonants and word[1] == "y":
        if word[0] in consonants and word.startswith("y", 1):
            new_word = (word + word[0])[1:]
            print(new_word + pig_latin_adding)
            return new_word + pig_latin_adding
        # if word[0] in consonants and word[1] in consonants and word[2] == "y":
        if word[0] in consonants and word[1] in consonants and word.startswith("y", 2):
            new_word = (word + word[:2])[2:]
            print(new_word + pig_latin_adding)
            return new_word + pig_latin_adding
        if word[0] in consonants and word[1] in consonants and word[2] in consonants and word.startswith("y", 3):
            new_word = (word + word[:3])[3:]
            print(new_word + pig_latin_adding)
            return new_word + pig_latin_adding

    

    # si un mot commence avec aucune ou plusieurs consonnes suivies de "qu", déplace ces consonnes à la fin du mot et ajoute "ay" à la fin
    # It would be simpler and safer to use a loop that goes and looks for the first vowel, wherever that may be, and then split the word there.
    # (The same holds for how you assume that a vowel 'y' will always be the second or third letter in the word.
    # Sometimes it's the fourth, as in spry or strychnine.)
        if word.startswith("qu"):
            new_word = (word + word[:2])[2:]
            print(new_word + pig_latin_adding)
            return new_word + pig_latin_adding
        if word.startswith("qu",1):
            new_word = (word + word[:3])[3:]
            print(new_word + pig_latin_adding)
            return new_word + pig_latin_adding
    # si un mot commence avec une ou plusieurs consonnes, déplace ces consonnes à la fin du mot et ajoute "ay" à la fin
        if word[0] in consonants and word[1] in consonants and word[2] in consonants :
            new_word = (word + word[0] + word[1] + word[2])[3:]
            print(new_word + pig_latin_adding)
            return new_word + pig_latin_adding
        if word[0] in consonants and word[1] in consonants :
            new_word = (word + word[:2])[2:]
            print(new_word + pig_latin_adding)
            return new_word + pig_latin_adding
        if word[0] in consonants:
            new_word = (word + word[0])[1:]
            print(new_word + pig_latin_adding)
            return new_word + pig_latin_adding

    else:
        word_too_short = print("Votre mot est trop court.")
        return word_too_short

def translate(text):
    # translated_words = []
    # string_of_translated_words = ""
    # new_text = text.split(' ')
    # for word in new_text:
    #     string_of_translated_words += translate_word(word) + " "
    # string_of_translated_words_clean = string_of_translated_words.strip()
    # return string_of_translated_words_clean

    return ' '.join(map(translate_word, text.split()))



translate_word("strychnine")
# print(translate("voici une phrase"))
