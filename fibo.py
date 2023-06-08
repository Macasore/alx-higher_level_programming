def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a ,b = b, a+b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

# random.sample(range(2000), 10) this is to get random values between 0 and 2000 and fill 10 places
