def is_prime(num, memo):

    if num in memo:
        return True
    else:
        for prime in memo:

            if num % prime == 0:
                return False

        return True

def main():

    prime_list = [2]

    i = 3

    while len(prime_list) < 10001:

        if is_prime(i, prime_list):
            prime_list.append(i)

        i += 2

    print(memo[10000])

main()
        
