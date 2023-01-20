import concurrent.futures
import time
from threading import Lock

DECIMALS = [50 + x for x in range(1_000_000)]
LOCK = Lock()


def convert_decimal_to_binary(num):
    _decimal = num
    bits = []

    while num > 0:
        remainder = num % 2
        bits.append(remainder)
        num = num // 2
    bits.reverse()

    binary = ''
    for bit in bits:
        binary += str(bit)

    with LOCK:
        print(f"Decimal number {_decimal} converted to binary is: {binary}")


if __name__ == "__main__":
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(convert_decimal_to_binary, DECIMALS)

    duration_in_s = (time.time() - start_time)
    print(f"Finished in {duration_in_s} seconds")
