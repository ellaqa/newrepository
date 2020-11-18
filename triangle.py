import sys

from sys import argv

script, a, b, c = argv

if a + b <= c or a + c <= b or b + c <= a:
    print("Triangle is not existent")
elif a != b and a != c and b != c :
    print ("The triangle is scalene")
elif a == b == c:
    print ("The triangle is equilateral ")
else:
    print ("The triangle is isosceles")
