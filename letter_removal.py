def solve(st,k):  
    #############################################################################
    # Master Solution:
    # for l in sorted(st)[:k]:
    #     st=st.replace(l,'',1)
    # return st  
    #############################################################################    

    #############################################################################
    # My original solution:
    import string
    a = list(string.ascii_lowercase)
    aIndex = 0
    c = 1
    while c <= k:
        if st.count(a[aIndex]) > 0:  
            st = st.replace(a[aIndex], "", 1)
            c += 1
        elif st.count(a[aIndex]) == 0:
            aIndex += 1  
    return st
    #############################################################################
    
    # Sort characters in input string and loop first k characters
    # for chr in sorted(st)[:k]:
    #     # print (chr)
    #     st = st.replace(chr, "", 1)
    #     # print (st)
    # return st



print(solve('abracadabra', 8) == 'rdr')

# Test.assert_equals(solve('abracadabra', 1),'bracadabra')
# Test.assert_equals(solve('abracadabra', 2),'brcadabra')
# Test.assert_equals(solve('abracadabra', 6),'rcdbr')
# Test.assert_equals(solve('abracadabra', 8),'rdr')
# Test.assert_equals(solve('abracadabra', 50),'')