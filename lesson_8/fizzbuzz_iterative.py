# fizzbuzz example using plain loops
# https://en.wikipedia.org/wiki/Fizz_buzz

def fizzbuzz(num=16):
    """Generates fizzbuzz sequence"""
    result = []
    for count in range(1, num):
        if count % 3 == 0 and count % 5 == 0:
            result.append("FizzBuzz")
        elif count % 3 == 0:
            result.append("Fizz")
        elif count % 5 == 0:
            result.append("Buzz")
        else:
            result.append(count)

    return result

if __name__ == "__main__":
    print(fizzbuzz(num=30))
