# Jonny Derenge

f = open("2015/day06.txt")
lines = [line.rstrip() for line in f.readlines()]

plot = [[0] * 1000 for i in range(1000)]
plot2 = [[0] * 1000 for i in range(1000)]

def coord(instructone, instructtwo):
    a, b = instructone.split(',')
    c, d = instructtwo.split(',')
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    return [a, b, c, d]

for line in lines:
    
    instruct = line.split(' ')

    if instruct[0] == 'turn':
        a, b, c, d = coord(instruct[2], instruct[4])
        for x in range(a, c + 1):
            for y in range(b, d + 1):
                if instruct[1] == 'on':
                    plot[x][y] = 1
                    plot2[x][y] += 1
                else:
                    plot[x][y] = 0
                    # decrease plot2 (but not below 0)
                    plot2[x][y] -= 1
                    if plot2[x][y] < 0:
                        plot2[x][y] = 0

    else:
        a, b, c, d = coord(instruct[1], instruct[3])
        for x in range(a, c + 1):
            for y in range(b, d + 1):
                if plot[x][y] == 1:
                    plot[x][y] = 0
                else:
                    plot[x][y] = 1
                plot2[x][y] += 2

part1 = 0
for row in plot:
    for index in row:
        part1 += index

part2 = 0
for row in plot2:
    for index in row:
        part2 += index

print(part1)
print(part2)
