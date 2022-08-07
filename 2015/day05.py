# Jonny Derenge
from nis import match
import re as regex
from time import gmtime

f = open("2015/day05.txt")

lines = f.readlines()
counting_nice = 0
vowels = regex.compile(r"[aeiou]")
consec = regex.compile(r'([a-z])\1')
bad_string = regex.compile(r'ab|cd|pq|xy')
for line in lines:
    num =(len(vowels.findall(line)))
    if num >= 3:
        if consec.search(line) != None:
            if bad_string.search(line) == None:
                counting_nice += 1 # Increment good string
print(counting_nice)