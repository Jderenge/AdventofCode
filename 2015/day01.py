f = open("2015/day01.txt")

lines = f.readlines()
pos = 0
counting = 1
part2answer = 0

for line in lines:
    for character in line:
        if character == '(':
            pos = pos + 1
        else:
            pos = pos -1
            if pos == -1 and part2answer == 0: # Needs to be the first time Santa enters the basement
                part2answer = counting 
                
        counting += 1

print(pos)
print(part2answer)
# Jonny Derenge