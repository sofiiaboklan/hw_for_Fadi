# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13...

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def main():
    print(fib(int(input("what fib do you want?: "))))

if __name__ == '__main__':
    main()
