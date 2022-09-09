def is_prime(num, memo):

    if num in memo:
        return True
    else:
        for prime in memo:

            if num % prime == 0:
                return False

        return True

def gather_the_primes(limit):

    prime_list = [2]
    i = 3

    while i < limit:


        if is_prime(i, prime_list):
            prime_list.append(i)

        i += 2

        

    return prime_list


def sieve_of_sundaram(limit):

    k = int((limit - 2)/2)
    a = [0] * (k+1)
    prime_list = []

    

    for i in range( 1, k + 1):
        j = i
        while (i  + j + 2*i*j <= k):
            a[i + j + 2*i*j] = 1
            j += 1

    if limit > 2:
        prime_list.append(2)

    for i in range(1, k + 1):
        if a[i] == 0:
            prime = 2 * i + 1
            prime_list.append(prime)

    return prime_list
        
        

        
def main():

    #print(gather_the_primes(100))
    print(sum(sieve_of_sundaram(2000000)))

main()
