def multiples_of_three(num):

    sum = 0
    for n in range(num):
        if n % 3 == 0 or n % 5 == 0:
            sum += n
    return sum

def main():
    print(multiples_of_three(10))
    print(multiples_of_three(1000))

main()
    
