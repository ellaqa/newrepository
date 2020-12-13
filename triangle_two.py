from sys import argv
script, a, b, c = argv

#@pytest.fixture


def triangle(a,b,c):
    if a + b <= c or a + c <= b or b + c <= a:
        return 'not_existent'
    elif a != b and a != c and b != c:
        return 'scalene'
    elif a == b == c:
        return 'equilateral'
    else:
        return 'isosceles'
