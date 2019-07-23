# Weight for weight Codewars Kata
# Example:
# "56 65 74 100 99 68 86 180 90" ordered by numbers weights
# becomes: "100 180 90 56 65 74 68 86 99"


# TODO: Finish this...
def order_weight(strng):
    # your code
    print(strng)
    list = strng.split()
    print(list)
    print(type(list))

    print(len(list[0]))
    print(list[1])
    print(type(list[0][0]))

    print(list[0] + list[1])


if __name__ == '__main__':
    order_weight('56 65 74 100 99 68 86 180 90')
