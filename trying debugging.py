def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

def main():
    num = 10
    print(f"Fibonacci of {num}: {fibonacci(num)}")

if __name__ == "__main__":
    main()
