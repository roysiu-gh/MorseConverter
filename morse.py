import csv

input("message: ")

morse_dict = {}
reader = csv.reader(open('morse_seq.csv', 'r'))
for key, value in reader:
    morse_dict[key] = value

print(morse_dict)

morse_enc = [ morse_dict[x] for x in message ]
print(morse_enc)

raw_morse = []

for letter in morse_enc:
    print (letter)
    for element in letter:
        print(element)
        if element == ".":
            raw_morse.append([1, True])
        elif element == "-":
            raw_morse.append([3, True])
        elif element == " ":
            raw_morse.append([1, False])
        else:
            raise ValueError
        raw_morse.append([1, False])
    raw_morse.append([2, False])

print(raw_morse,"\n")

compact_morse = [[None, None]]

for index, item in enumerate(raw_morse):
    if item[1] == compact_morse[-1][1]:
        compact_morse[-1][0] += item[0]
    else:
        compact_morse.append(item)

compact_morse = compact_morse[1:]
print(compact_morse)