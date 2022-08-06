# fizzbuzz example using list comprehension and logical expression evaluation order
# https://en.wikipedia.org/wiki/Fizz_buzz


def fizzbuzz(num=16):
    """Generates fizzbuzz sequence"""
    return [
        i % 3 == 0 and i % 5 == 0 and "FizzBuzz"
        or i % 3 == 0 and "Fizz"
        or i % 5 == 0 and "Buzz"
        or i
        for i in range(1, num)
    ]

if __name__ == "__main__":
    print(fizzbuzz(30))
