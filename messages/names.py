from random import randint


def get_generic_first_name():

    consonants  =["q", "w", "r", "t", "y", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
    vowels      =["e", "u", "i", "o", "a"]
    fPrefixes   =["Flo", "Lou", "La", "Es", "Be", "Vi", "In", "Fra", "Lov", "Je", "Col", "Ju", "Ali", "Lei", "Bra", "Tob", "Mas", "Row", "Ju", "Fi", "She", "Ja", "Av", "Lau", "Arc", "Ste", "Bri", "Moe", "Enr", "Ale"]
    fSuffixes   =["es", "on", "la", "ra", "iam", "am", "nce", "cie", "cey", "me", "ia", "et", "pe", "le", "ny", "vy", "ty", "py", "lia", "on", "se", "ah", "tin", "nn", "ob", "ton", "de", "gh", "ah", "die"]
    first = ""

    fLength = randint(0,8 - 3) + 3
    sucCons=0
    sucVows=0
    fName=""

    #gen first name
    for i in range(0,fLength):
        choice = randint(0,2)

        #Randomly add a prefix to name
        if i == 0:
            pre=randint(0,2)

            if pre == 1:
                fName=fName+fPrefixes[randint(0,len(fPrefixes)-1)]
                i=fLength-len(fName)

        #decides to choose consonant or vowel
        if choice == 0 and sucCons < 2 or sucVows >= 1:
            fName=fName+consonants[randint(0,len(consonants)-1)]
            sucCons+=1
            sucVows=0
        else:
            fName=fName+vowels[randint(0,len(vowels)-1)]
            sucCons=0
            sucVows+=1

        #Randomly add a suffix to name (last 3 letters)
        if (fLength-i) == 3:
            suff=randint(0,2)

            if suff == 1:
                fName=fName+fSuffixes[randint(0,len(fSuffixes)-1)]
                i=fLength

    first = fName.capitalize()

    return first

def get_generic_last_name():

    consonants  =["q", "w", "r", "t", "y", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
    vowels      =["e", "u", "i", "o", "a"]
    lPrefixes   =["Sm", "Jo", "Wil", "Bro", "Da", "Mil", "Ta", "Mo", "Jac", "And", "Whi", "Ha", "Tho", "Ga", "Rob", "Cla", "Ha", "Al", "He", "San", "Rod", "Dom", "Dad", "Tor", "Jo", "Ste", "Cam", "Be", "Mur", "Pur"]
    lSuffixes   =["es", "on", "th", "te", "is", "in", "son", "ez", "cia", "len", "dez", "ng", "re", "tin", "ing", "ee", "ers", "ed", "ox", "ra", "ans", "ker", "ok", "ed", "ris", "ait", "ips", "ray", "oss", "man"]
    last = ""

    lLength = randint(0,9-3)+3
    sucCons=0
    sucVows=0
    lName=""

    #generate last name
    for i in range(0,lLength):
        choice = randint(0,2)

        #Randomly add a prefix to name
        if i == 0:
            pre=randint(0,2)

            if pre == 1:
                lName=lName+lPrefixes[randint(0,len(lPrefixes)-1)]
                i=lLength-len(lName)


        #decides to choose consonant or vowel
        if choice == 0 and sucCons < 2 or sucVows >= 2:
            lName=lName+consonants[randint(0,len(consonants)-1)]
            sucCons+=1
            sucVows=0
        else:
            lName=lName+vowels[randint(0,len(vowels)-1)]
            sucCons=0
            sucVows+=1

        #Randomly add a suffix to name (last 3 letters)
        if (lLength-i) == 3:
            suff=randint(0,2)

            if suff == 1:
                lName=lName+lSuffixes[randint(0,len(lSuffixes)-1)]
                i=lLength

    last = lName.capitalize()

    return last
