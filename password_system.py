def help_zoom(key):
    print(len(key))

    key_len = len(key)

    print(key[0: key_len // 2: 1])
    left = key[0: key_len // 2: 1]
    print(left)

    print(key[key_len: key_len // 2: -1])
    right = key[key_len: key_len // 2: -1]
    print(right)

    print(left == right)

    if key[0: key_len // 2: 1] == key[key_len: key_len // 2: -1]:
        return 'Yes'
    else:
        return 'No'


# FIXME: FIx this test case
print(help_zoom([1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1]))

# Test.describe("Basic tests")
# Test.assert_equals(help_zoom([1, 1, 0, 0, 0, 0, 0, 1, 1]), "Yes")
# Test.assert_equals(help_zoom([1, 1, 0, 0, 0, 0, 1, 1, 0]), "No")
# Test.assert_equals(help_zoom([1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1]), "Yes")
# Test.assert_equals(help_zoom([1, 0, 1, 1, 0, 0, 0, 0, 0]), "No")
# Test.assert_equals(help_zoom([1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1]), "No")
