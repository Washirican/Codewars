# --------------------------------------------------------------------------- #
# Script Title: Cyclops numbers
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-09-18, Initial release
# --------------------------------------------------------------------------- #


def cyclops(n):
    print(len(bin(n)))
    print(type(bin(n)))
    print(bin(n))
    print(bin(n).replace('0b', ''))

    binary_n = bin(n).replace('0b', '')
    print(len(binary_n))
    if len(binary_n) % 2 == 0:
        return False


    return binary_n


if __name__ == '__main__':
    print(cyclops(10))
