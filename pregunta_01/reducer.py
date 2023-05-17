#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

count = {}
for credit_history in sys.stdin:
    if credit_history in count:
        count[credit_history] += 1
    else:
        count[credit_history] = 1

for credit_history, value in count.items():
    print(credit_history.rstrip() + '\t' + str(value))