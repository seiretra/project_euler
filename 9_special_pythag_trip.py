from math import sqrt


def is_odd(num):

    return num % 2 != 0

def is_even(num):

    return num % 2 == 0

def is_both_odd(a,b):

    return is_odd(a) is is_odd(b)

def can_make_triple(a,b):

    if a < b:
        c = sqrt(a**2 + b**2)

        if int(c) == c:

            return int(c)
    return False

def make_stifel_triple(a,b):

    sides = [b]
    sides.append(a + b*a)
    sides.append(can_make_triple(sides[0],sides[1]))
    sides.sort()
    return sides

def gcd(a,b):

    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    

    
def main():

    
        

    
main()
