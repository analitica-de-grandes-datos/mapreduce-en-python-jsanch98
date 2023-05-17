#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

count = {}
for month in sys.stdin:
    if month in count:
        count[month].append(1)
    else:
        count[month] = [1]

for month, val in count.items():
    print(month.rstrip() + '\t' + str(len(val)))