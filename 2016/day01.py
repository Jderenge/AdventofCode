# Jonny Derenge
f = open("2016/day01.txt")
lines=[line.rstrip() for line in f.readlines()]

angle =90
coords = [0, 0]
visited = []
for line in lines:
    for instruction in line.split(", "):
        angle +=  90 if instruction [0] == 'L' else -90
       
        angle = 0 if angle == 360 else angle
        angle = 270 if angle == -90 else angle            
        if angle == 0:
            coords[0] += int(instruction[1::])
        if angle == 90:
            coords[1] += int(instruction[1::])
        if angle == 180:
            coords[0] -= int(instruction[1::])
        if angle == 270:
            coords[1] -= int(instruction[1::])
            
        visited.append((coords[0], coords[1]))
visited = [i for i in visited if visited.count(i) > 1][0]
print("Part 1: " + str(sum([abs(i) for i in coords])))
