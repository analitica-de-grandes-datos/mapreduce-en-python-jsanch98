#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

count = {}
for purpose_amount in sys.stdin:
    purpose, amount = purpose_amount.split(',')
    if purpose in count:
        count[purpose].append(int(amount))
    else:
        count[purpose] = [int(amount)]

for purpose, value in count.items():
    print(purpose.rstrip() + '\t' + str(max(value)))