def equilateral(sides):
    a, b, c = sides
    if 0 not in [a, b, c]:
        if (a + b >= c) and (b + c >= a) and (a + c >= b):
            if (a == b) and ( a == c) and (b == c):
                return True
    return False
        
def isosceles(sides):
    a, b, c = sides
    if 0 not in [a, b, c]:
        if (a + b >= c) and (b + c >= a) and (a + c >= b):
            if (a == b) or (b == c) or (a == c):
                return True
    return False

def scalene(sides):
    a, b, c = sides
    if 0 not in [a, b, c]:
        if (a + b >= c) and (b + c >= a) and (a + c >= b):
            if (a != b) and (b != c) and (a != c):
                return True
    return False
