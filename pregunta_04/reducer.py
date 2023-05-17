#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

count = {}
for letter in sys.stdin:
    if letter in count:
        count[letter].append(1)
    else:
        count[letter] = [1]

for letter, val in count.items():
    print(letter.rstrip() + ',' + str(len(val)))