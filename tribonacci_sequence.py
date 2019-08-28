# --------------------------------------------------------------------------- #
# Script Title: Tribonacci Sequence
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-08-14, Initial release
# --------------------------------------------------------------------------- #


# -- Processing --#
def tribonacci(signature, n):
    """
    :param signature:
    :desc    :  This function returns the nth value in the Fibonacci Series (starting with zero index)
    :param  n: Series value to be returned
    :type   n: int
    :return :  Returns the nth value in the series
    :rtype  :   list
    """
    # signature = [0, 1]
    if n == 0:
        return []
    elif n < 3:
        return signature[:n]
    else:
        for x in range(3, n):
            signature.append(signature[x - 3] + signature[x - 2] + signature[x - 1])
        return signature


n = 10
print('Series: ', tribonacci([1, 1, 1], n))
print([1, 1, 1, 3, 5, 9, 17, 31, 57, 105] == tribonacci([1, 1, 1], n))

