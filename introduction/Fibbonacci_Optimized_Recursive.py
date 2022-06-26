def fib(n, memo = {}):
    if(n in memo):
        return memo[n]
    if(n <= 2):
        return 1
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

number = int(input("Enter a number: "))
answer = fib(number)
print("The fibonnaci of %d is %d" % (number, answer))
