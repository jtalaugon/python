def fib(n):
    if(n <= 2):
        return 1
    return fib(n - 1) + fib(n - 2)
number = int(input("Enter a number: "))
answer = fib(number)
print("The fibonnaci of %d is %d" % (number, answer))
