def is_palindrome(num):
    num_string = str(num)
    return num_string[:len(num_string)//2] == num_string[-1:len(num_string)//2 - 1:-1]

def main():

    palindromes = []
    for i in range(999,99, -1):
        for j in range(999, 99, -1):
        
            if is_palindrome(i * j):
                palindromes.append(i* j)


    print(max(palindromes))


main()

