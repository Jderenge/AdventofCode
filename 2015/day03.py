# Jonny Derenge
from enum import unique

f = open("2015/day03.txt")

lines = f.readlines()

coord =  [(0,0)]
rcoord = [(0,0)]

for line in lines:
    counter = 0
    for character in line:
        if character == '<':
            # coord.append((coord[-1][0] -1, coord[-1][1]))
            if counter % 2 == 0:
                coord.append((coord[-1][0] -1, coord[-1][1]))
            else:
                rcoord.append((rcoord[-1][0] -1, rcoord[-1][1]))
        elif character == '>':
            # coord.append((coord[-1][0] +1, coord[-1][1]))
            if counter % 2 == 0:
                coord.append((coord[-1][0] +1, coord[-1][1]))
            else:
                rcoord.append((rcoord[-1][0] +1, rcoord[-1][1]))
        elif character == '^':
            # coord.append((coord[-1][0], coord[-1][1] +1))
            if counter % 2 == 0:
                coord.append((coord[-1][0], coord[-1][1] +1))
            else:
                rcoord.append((rcoord[-1][0], rcoord[-1][1] +1))
        else:
            # coord.append((coord[-1][0], coord[-1][1] -1))
            if counter % 2 == 0:
                coord.append((coord[-1][0], coord[-1][1] -1))
            else:
                rcoord.append((rcoord[-1][0], rcoord[-1][1] - 1))
        counter += 1

unique = len(list(set(coord + rcoord)))
print(unique)