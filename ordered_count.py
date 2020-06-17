# --------------------------------------------------------------------------- #
# D. Rodriguez, 2019-08-27
# --------------------------------------------------------------------------- #
"""
Count the number of occurrences of each character and return it as a list of
tuples in order of appearance.
"""


def ordered_count(input):
    output = []
    # In alphabetical order
    # for letter in sorted(set(input)):
    #     output.append(tuple((letter, input.count(letter))))

    # In order of appearance
    for letter in input:
        print(output)
        print(letter)


        if letter not in output[:][0]:
            output.append(tuple((letter, input.count(letter))))

    return output


if __name__ == '__main__':
    print(ordered_count('abracadabra'))
