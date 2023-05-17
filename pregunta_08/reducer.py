#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

count = {}
for letter_value in sys.stdin:
    if letter_value != '\n':
        letter, value = letter_value.split(',')
        value = value.rstrip()
        if letter in count:
            count[letter].append(float(value))
        else:
            count[letter] = [float(value)]

for letter, value in count.items():
    print(letter.rstrip() + '\t' + str(sum(value)) + '\t' + str(sum(value)/len(value)))