def help_zoom(key):
    #In work
    
    #your code here
   
    print (key[:len(key)//2])

    print (key[len(key)//2:len(key)])

    print (len(key)//2)

    if len(key)%2 == 0:
        # Even
        print ("Even")
    else:
        # odd
        print ("Odd")
        # left = 

    # for i in key:
    #     for j in range(len(key),0,-1):
    #         print (j)








help_zoom([1, 1, 0, 0, 0, 0, 0, 1, 1 ])

# Test.describe("Basic tests")
# Test.assert_equals(help_zoom([1, 1, 0, 0, 0, 0, 0, 1, 1 ]) , "Yes")
# Test.assert_equals(help_zoom([1, 1, 0, 0, 0, 0, 1, 1, 0 ]) , "No")
# Test.assert_equals(help_zoom([1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1 ]) , "Yes")    
# Test.assert_equals(help_zoom([1, 0, 1, 1, 0, 0, 0, 0, 0 ]) , "No")
# Test.assert_equals(help_zoom([1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1 ]) , "No")