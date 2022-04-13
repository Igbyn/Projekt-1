TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

space = "=" * 50

registrovani = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}

try:
    if registrovani[input("username: ")] == input("password: "):
        print(space)
        print("Welcome to the app, bob\nWe have 3 texts to be analyzed.")
        print(space)
        number = int(input("Enter a number btw. 1 and 3 to select: ")) - 1
        if number > 3 or number < 0:
            print("wrong number")
            exit()
        titlecase = 0
        uppercase = 0
        lowercase = 0
        numericstr = 0
        sum = 0
        length = {"1":0}
        for word in TEXTS[number].split():
            if word.istitle():
                titlecase += 1
            elif word.isupper():
                uppercase += 1
            elif word.islower():
                lowercase += 1
            elif word.isnumeric():
                numericstr += 1
                sum += int(word)
            try:
                length[str(len(word))] += 1
            except:
                last_n = int(list(length.keys())[-1])
                for n in range(len(word) - last_n):
                    length.update({str(last_n + n + 1):0})
                length.update({str(len(word)):1})
        print(space)
        print(f"There are {len(TEXTS[number].split())} words in the selected text.")
        print(f"There are {titlecase} titlecase words.")
        print(f"There are {uppercase} uppercase words.")
        print(f"There are {lowercase} lowercase words.")
        print(f"There are {numericstr} numeric strings.")
        print(f"The sum of all the numbers {sum}")
        print(space)
        longest = 0
        for word in length:
            if int(length[word]) > longest:
                longest = int(length[word])
        print(f"LEN|{'OCCURENCES': ^{longest + 1}}|NR")
        print(space)
        for word in length:
            print(f"{word: >3}|{'*'*length[word]: <{longest + 1}}|{length[word]: <2}")
    else:
        print("wrong password")
except KeyError:
    print("unregistered user, terminating the program..")