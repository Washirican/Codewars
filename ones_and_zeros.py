def binary_array_to_number(arr):

    #** Master Solution
    return int("".join(map(str, arr)), 2)
    
    # My Solution 
     # maxPower = len(arr)-1
    # decVal = 0
    # binVal = ""
    # for x in arr:
    #     binVal = binVal + str(x)
    #     decVal = decVal + x * 2**maxPower
    #     print (x, "*", 2, "^", maxPower, "=", x * 2**maxPower)               
    #     maxPower = maxPower - 1
    # print("\n\nBinary Number: ", binVal, "Equals Decimal Number:", decVal)
    # return decVal



#** Test Code:
print(binary_array_to_number([1,1,1,1]))

# Test.assert_equals(binary_array_to_number([0,0,0,1]), 1)
# Test.assert_equals(binary_array_to_number([0,0,1,0]), 2)
# Test.assert_equals(binary_array_to_number([1,1,1,1]), 15)
# Test.assert_equals(binary_array_to_number([0,1,1,0]), 6)