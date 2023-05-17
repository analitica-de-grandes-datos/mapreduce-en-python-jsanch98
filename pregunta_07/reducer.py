#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

records = []

for line in sys.stdin:
    if line != '\n':
        letter, date, num = line.split('   ')
        record = (letter, date, num.rstrip())
        records.append(record)

records = sorted(records, key=lambda record: (record[0], int(record[2])))

for record in records:
    print(f'{str(record[0])}   {record[1]}   {record[2]}')