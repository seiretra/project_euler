def fib(n, memo):
    if n < 2:
        return memo[n]
    else:
        if n >= len(memo):
            f = fib(n-1, memo) + fib(n-2, memo)
            memo.append(f)
            return f
        else:
            return memo[n]

def main():

    n = 0
    memo = [1,2]
    sum = 0

    while fib(n, memo) < 4000000:
        if fib(n, memo) % 2 == 0:
            sum += fib(n, memo)
        n +=1

    print(sum)

def better_fib():

    f1 = 1
    f2 = 1
    sum = 0
    while f1 + f2 < 4000000:

        if (f1 + f2) % 2 == 0:
            sum += f1 + f2
        temp = f1 + f2
        f1 = f2
        f2 = temp
        
    return sum


print(better_fib())
            
