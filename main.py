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

users = {'bob' : '123', 'ann' : 'pass123', 'mike' : 'password', 'liz' : 'pass123'}

print('-'*40)
print('Welcome to the app. Please log in:')
print('-'*40)

username = input('USERNAME: ')
password = input('PASSWORD: ')

print('-'*40)

if users.get(username) != password:
    print('Wrong username or password.')
    quit()

choice = int(input('''We have 3 texts to be analyzed.
Enter a number btw. 1 and 3 to select: '''))

print('-' * 40)

number_of_choice = TEXTS[choice-1]
dirty_words = number_of_choice.split()

words = []

while dirty_words:
    word = dirty_words.pop()
    word = word.strip('.,')
    if word: words.append(word)

number_of_words = len(words)
number_of_first_letter = 0
number_of_big_words = 0
number_of_small_words = 0
number_of_numeric = 0
counts = {}
num_sum = 0

while words:
    if words[0].istitle():
        number_of_first_letter += 1
    elif words[0].isupper():
        number_of_big_words += 1
    elif words[0].islower():
        number_of_small_words += 1
    elif words[0].isnumeric():
        number_of_numeric += 1
        num_sum = num_sum + float(words[0])
    l= len(words[0])
    counts[l] = counts.get(l, 0) + 1

    words = words[1:]

print('There are', number_of_words, 'in the selected text')
print('There are', number_of_first_letter, 'titlecase words')
print('There are', number_of_big_words, 'uppercase words')
print('There are', number_of_small_words, 'lowercase words')
print('There are', number_of_numeric, 'numeric strings')

print('-' * 40)


lengths = sorted(counts)
i= 0
while i < len(lengths):
    length = lengths[i]
    frequency = counts[length]
    if len(str(length)) == 1:
        str_len = ' ' + str(length)
    else:
        str_len = str(length)
    print(str_len, '*' * frequency, frequency)
    i = i + 1

print('-' * 40)

print('If we summed all the numbers in this text we would get: ', num_sum)

print('-' * 40)