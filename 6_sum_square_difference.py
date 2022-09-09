def brute_force_ssd(num):

    sum_of_squares = 0
    square_sum = 0
    
    for i in range(1, num +1):
        sum_of_squares += i ** 2
        square_sum += i

    square_sum **= 2

    diff = square_sum - sum_of_squares

    return diff


def sum_square_difference(num):

    square_sum = ((num ** 2) *((num + 1) **2)) // 4
    sum_of_squares = (num * ( num + 1) * (2 * num + 1)) // 6

    return square_sum - sum_of_squares

def main():

    print(brute_force_ssd(10))
    print(sum_square_difference(10))
    

main()
