import math



def is_prime(num):

    if num == 0:
        return False
    elif num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(num)) + 2):
            if num % i == 0:
                return False
    return True

def greatest_power_prime(prime, target):

    power = 0
    val = prime

    while val < target:
        power += 1
        val *= prime
        
    return power


def smallest_multiple(num):

    multiple = 1

    for i in range(2, num + 1):
        if is_prime(i):
            power = greatest_power_prime(i, num)
            multiple *= i ** power
    return multiple

def main():
    
    print(smallest_multiple(20))


main()
            
        
