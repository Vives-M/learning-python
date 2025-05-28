def equilateral(sides):
    # a, b, c = sorted(sides)
    # return 0 < a == c
    a = sides[0]
    b= sides[1]
    c = sides[2]
    if (a + b) >= c and (b + c) >= a and (a + c) >= b and a != 0 and b != 0 and c != 0:
        if a == b and a == c:
            return True
        return False
    return False

def isosceles(sides):
    # a, b, c = sorted(sides)
    # return 0 < a and c < a + b and b in (a, c)
    a = sides[0]
    b= sides[1]
    c = sides[2]
    if (a + b) >= c and (b + c) >= a and (a + c) >= b and a != 0 and b != 0 and c != 0:
        if a == b or a == c or b == c:
            return True
        return False
    return False


def scalene(sides):
    # a, b, c = sorted(sides)
    # return 0 < a < b < c < a + b
    a = sides[0]
    b= sides[1]
    c = sides[2]
    if (a + b) >= c and (b + c) >= a and (a + c) >= b and a != 0 and b != 0 and c != 0:
        if a != b and a != c and b !=c:
            return True
        return False
    return False
