import multiprocessing
import time

NUMBERS = [15_000_000 + x for x in range(100)]


def is_number_prime(num):
    if num <= 1:
        print(f"{num} is not a prime number")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")


if __name__ == "__main__":
    start_time = time.time()

    with multiprocessing.Pool() as pool:
        pool.map(is_number_prime, NUMBERS)

    duration_in_s = (time.time() - start_time)
    print(f"Finished in {duration_in_s} seconds")
