
def camelCasing():
    sentennce = input("Enter a sentence: ").split()
    print(sentennce)


    rep = ""
    for letter in range(len(sentennce)):
        if sentennce[letter][1].isupper() and sentennce[letter][0].islower():
            rep += sentennce[letter].lower()
        elif sentennce[letter][0:3].islower():
            rep += sentennce[letter].title()
        elif sentennce[letter][-2].isupper():
            rep += sentennce[letter].title()
        elif sentennce[letter][0:2].islower():
            rep += sentennce[letter].title()

    return rep

if __name__ == '__main__':

    print(camelCasing())


