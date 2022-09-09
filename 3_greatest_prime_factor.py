import math

def largest_prime_factor(num):

    temp = num

    while temp % 2 == 0:

        temp = temp //2

    for n in range (3, int(math.sqrt(num)) + 1 , 2):
        while temp % n == 0:
            if temp == n:
                return temp
            else:
                temp = temp //n
        
    

print(largest_prime_factor(60110851475143))
print(60110851475143 % 11) 
