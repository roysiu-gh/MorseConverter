import csv
import winsound, time
frequency = 2500
duration = 100 # Milliseconds

dot = "10"
dash = "1110"
sep = "00"

with open("morse_seq.csv", "r") as f:
    csvf = csv.reader(f)
    codes = {row[0]:row[1] for row in csvf}

morse_enc = ""
for i in "Hello World".lower():
    morse_enc += codes[i] + " "

print(morse_enc)

bin_enc = ""
for i in morse_enc:
    if i == ".":
        bin_enc += dot
    elif i == "-":
        bin_enc += dash
    elif i == " ":
        bin_enc += sep

print(bin_enc)

#sig_separator = 0
#let_separator = 1
#word_separator = 2
#dot = 3
#dash = 4

foo = "111000111011111100011001001010110101101011011000010010101111010100010100001010111010111100011110101010001010111010111010111101010000000000101111111100100101010110110101111110101000110101000101110101"

lis = [[None]]
for i in bin_enc:
    i = int(i)
    if lis[-1][0] == i:
        lis[-1][1] += 1
    else:
        lis.append([i, 1])

del lis[0]

print(lis)

for item in lis:
    print(item)
    if int(item[0]):
        winsound.Beep(frequency, duration*item[1])
    else:
        time.sleep(duration*item[1]/1000)
