#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for credit in sys.stdin:
    credit_history = credit.split(',')[2]
    print(f'{credit_history.rstrip()}')
