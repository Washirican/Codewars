# Weight for weight Codewars Kata

def order_weight(strng):
    # your code
    list = strng.split()
    map_list = map(sum, list)

    return map_list


if __name__ == '__main__':
    result = order_weight('56 65 74 100 99 68 86 180 90')
    # '100 180 90 56 65 74 68 86 99'

    print(result)

    for item in result:
        print(item)
        print('This is the result:')
