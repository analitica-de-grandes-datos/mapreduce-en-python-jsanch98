#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

shuffle = {}

for line in sys.stdin:
    if line != '\n':
        key, value = line.split(',')
        shuffle[key] = value.rstrip()

shuffle = sorted(shuffle.items(), key=lambda x: x[1])

# Format
for key, value in shuffle:
    print(f'{key},{value}')