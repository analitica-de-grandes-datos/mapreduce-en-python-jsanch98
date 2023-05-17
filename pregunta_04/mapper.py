#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    line_splitted = line.split('   ')
    letter = line_splitted[0]
    print(f'{letter}')