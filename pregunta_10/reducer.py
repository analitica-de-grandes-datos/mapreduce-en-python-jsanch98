#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

groups = {}
for record in sys.stdin:
    if record != '\n':
        splitted_record = record.split('\t')
        number = int(splitted_record[0])
        letters = splitted_record[1].rstrip().split(',')
        for letter in letters:
            if letter not in groups:
                groups[letter] = [number]
            else:
                groups[letter].append(number)

sorted_records = sorted(groups.items(), key=lambda x: x[0])

for record in sorted_records:
    print(f'{record[0]}'+ '\t' +f'{",".join(list(map(lambda x: str(x),sorted(record[1]))))}')