import time

NUMBERS = [40, 500, 200, 100, 50, 55, 20, 80, 90, 99, 7, 8, 9, 60]


def calculate_factorial(number):
    if number < 1:
        return 1
    else:
        _factorial = number * calculate_factorial(number - 1)
        return _factorial


if __name__ == "__main__":
    start_time = time.time()

    for number in NUMBERS:
        factorial = str(calculate_factorial(number))
        print(f"Factorial of {number}: {factorial}")

    duration_in_ms = (time.time() - start_time) * 1000
    print(f"Finished in {duration_in_ms} milli seconds")
