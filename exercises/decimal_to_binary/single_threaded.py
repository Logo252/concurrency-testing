import time

DECIMALS = [50 + x for x in range(1_000_000)]


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

    print(f"Decimal number {_decimal} converted to binary is: {binary}")


if __name__ == "__main__":
    start_time = time.time()

    for decimal in DECIMALS:
        convert_decimal_to_binary(decimal)

    duration_in_s = (time.time() - start_time)
    print(f"Finished in {duration_in_s} seconds")
