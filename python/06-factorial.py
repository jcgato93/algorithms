def factorial(n):
    if n == 0:
        return 1
    # recursive function
    return n * factorial(n-1)


if __name__ == "__main__":
    print("The value of 0! is {}".format(factorial(0)))
    print("The value of 5! is {}".format(factorial(5)))