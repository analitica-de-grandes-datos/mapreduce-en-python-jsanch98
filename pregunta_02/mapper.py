#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for credit in sys.stdin:
    credit_splitted = credit.split(',')
    purpose = credit_splitted[3]
    amount =  credit_splitted[4]
    print(f'{purpose},{amount}')