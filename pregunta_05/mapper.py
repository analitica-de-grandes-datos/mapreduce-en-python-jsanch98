#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    line_splitted = line.split('   ')
    month = line_splitted[1].split('-')[1]
    print(f'{month}')