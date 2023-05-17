#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

records = []
for record in sys.stdin:
    if record != '\n':
        value = record.split('   ')[2]
        value = int(value.rstrip())
        records.append((record, value))

sorted_records = sorted(records, key=lambda x: x[1])[:6]

for record in sorted_records:
    print(record[0].rstrip())