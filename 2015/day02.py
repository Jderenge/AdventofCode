# Jonny Derenge

f = open("2015/day02.txt")

lines = f.readlines()
sqfeet = 0
total = 0

for line in lines:
    len, height, width = [int(i) for i in line.rstrip().split('x')]
    area = len * height * width
    face1, face2, face3 = (len * height), (len * width), (width * height)

# find the sides with the 2 smallest parimeters 
# create array of dimensions
# sort array
# use first 2 elements

    dimensions = [len, height, width]
    dimensions.sort()
    smallest = dimensions[0]
    almostsmallest = dimensions[1]

# add them together, multiply by two
    perimeter = 2 * (smallest + almostsmallest)
# add the length of the bow, (volume of present, base * height)
    base = width * len
    volume = base * height
    total = total + volume + perimeter
# print total
print(total)
'''
    # find smallest face, and add it to area
    if face1 <= face2 and face1 <= face3:
        trim = face1
    elif face2 <= face1 and face2 <= face3:
        trim = face2
    else:
        trim = face3
    area = 2 * (face1 + face2 + face3)
    area = area + trim
    sqfeet = sqfeet + area

print(sqfeet)'''