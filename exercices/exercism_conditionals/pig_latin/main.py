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



def translate_single_word(word):
    """
    :param word: string - le word à traduire
    :result: string - le word traduit
    """
    vowels = ["a", "e", "i", "o", "u"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x" ,"y" ,"z"]
    pig_latin_adding = "ay"
    word_length = len(word)
    # print(f"word = {word} and word length = {word_length}")
    if word_length > 1:
        # print(len(word))
    # si un mot commence avec une voyelle ou avec "xr" ou "yt", ajoute "ay" à la fin du mot
        # if word[0] in vowels or word[0:2] == "xr" or word[0:2] == "yt":
        #     return word + pig_latin_adding
        if word[0] in vowels or word.startswith("xr") or word.startswith("yt"):
            # print(word + pig_latin_adding)
            return word + pig_latin_adding
    # si un mot commence avec une ou plusieurs consonnes suivies de "y", déplace les consonnes précédant le "y" à la fin du mot et ajoute "ay" à la fin

    # Ancien code sans boucle while (trop redondant et non exhaustif):
        # if word[0] in consonants and word[1] == "y":
        # if word[0] in consonants and word.startswith("y", 1):
        #     new_word = (word + word[0])[1:]
        #     print(new_word + pig_latin_adding)
        #     return new_word + pig_latin_adding
        # # if word[0] in consonants and word[1] in consonants and word[2] == "y":
        # if word[0] in consonants and word[1] in consonants and word.startswith("y", 2):
        #     new_word = (word + word[:2])[2:]
        #     print(new_word + pig_latin_adding)
        #     return new_word + pig_latin_adding
        # if word[0] in consonants and word[1] in consonants and word[2] in consonants and word.startswith("y", 3):
        #     new_word = (word + word[:3])[3:]
        #     print(new_word + pig_latin_adding)
        #     return new_word + pig_latin_adding

        # Si un mot commence avec "qu", déplace "qu" à la fin du mot et ajoute "ay"
        if word.startswith("qu") :
            new_word = (word + word[:2])[2:]
            # print(f"le nouveau mot est {new_word + pig_latin_adding}")
            return new_word + pig_latin_adding

    # Nouveau code avec la boucle while :
    # Remarque du mentor : "It would be simpler and safer to use a loop that goes and looks for the first vowel, wherever that may be, and then split the word there.
    # (The same holds for how you assume that a vowel 'y' will always be the second or third letter in the word.
    # Sometimes it's the fourth, as in spry or strychnine.)"
    # Tant que la lettre est une consonne, la boucle continue.
    # - Si la lettre suivant la/les consonnes est un y, on renvoie le nouveau mot
    # - Si les lettres suivant la/les consonnes est un "qu", on renvoie le nouveau mot
    # (déplace les consonnes précédant le "y" ou le "qu" à la fin du mot et ajoute "ay" à la fin)
    # Sinon, on arrête la boucle
        n = 0
        while word[n] in consonants :
            # print(n, word[n])
            if word[n+1] == "y":
                # print(f"la {n+2}eme lettre est un y")
                new_word = (word + word[:n+1])[n+1:]
                # print(f"le nouveau mot est : {new_word + pig_latin_adding}")
                return new_word + pig_latin_adding
                break
             # si un mot commence avec une ou plusieurs consonnes, déplace ces consonnes à la fin du mot et ajoute "ay" à la fin
            elif word[n+1] in vowels:
                new_word = (word + word[:n+1])[n+1:]
                # print(f"le nouveau mot est {new_word + pig_latin_adding}")
                return new_word + pig_latin_adding
                break
            elif word.startswith("qu", n+1):
                # print("il y a un qu en n+1 !")
                new_word = (word + word[:n+3])[n+3:]
                # print(f"le nouveau mot est {new_word + pig_latin_adding}")
                return new_word + pig_latin_adding
                break
            # elif word[n+2] in vowels:
            #     # print("le mot ne comporte pas plusieurs consonnes avant un 'qu'")
            #     break
            else:
                n=n+1

    # Ancien code sans boucle while (trop redondant et non exhaustif):
        # if word.startswith("qu"):
        #     new_word = (word + word[:2])[2:]
        #     print(new_word + pig_latin_adding)
        #     return new_word + pig_latin_adding
        # if word.startswith("qu",1):
        #     new_word = (word + word[:3])[3:]
        #     print(new_word + pig_latin_adding)
        #     return new_word + pig_latin_adding


        # if word[0] in consonants and word[1] in consonants and word[2] in consonants :
        #     new_word = (word + word[0] + word[1] + word[2])[3:]
        #     print(new_word + pig_latin_adding)
        #     return new_word + pig_latin_adding
        # if word[0] in consonants and word[1] in consonants :
        #     new_word = (word + word[:2])[2:]
        #     print(new_word + pig_latin_adding)
        #     return new_word + pig_latin_adding
        # if word[0] in consonants:
        #     new_word = (word + word[0])[1:]
        #     print(new_word + pig_latin_adding)
        #     return new_word + pig_latin_adding

    else:
        return word

def translate_text(text):
   return ' '.join(map(translate_single_word, text.split()))


def translate(word):
    word_with_spaces = word.find(' ')
    if word_with_spaces == -1:
        return translate_single_word(word)
    else:
        return translate_text(word)

# print(translate_word("apple"))
# translate("quick fast run")
