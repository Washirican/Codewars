# Weight for weight Codewars Kata

def order_weight(strng):
    # your code
    list = strng.split()
    map_list = map(sum, list)

    return map_list


if __name__ == '__main__':
    result = order_weight('103 123 4444 99 2000')

    print(result)

    for item in result:
        print(item)
