

def fib(n):
    fn = 0
    fn1 = 0
    fn2 = 0
    for i in range (n):
        if(i == 1):
            fn = 1

        fn1 = fn
        fn = fn1 + fn2
        fn2 = fn1
    return fn


Number = int(input("Enter a number: "))
result = fib(Number)

print("The fibonnaci of %d is %d" % (Number, result))

