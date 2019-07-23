def likes(names):
    #your code here
    # Master Code:
    # n = len(names)
    # return {
    #     0: 'no one likes this',
    #     1: '{} likes this', 
    #     2: '{} and {} like this', 
    #     3: '{}, {} and {} like this', 
    #     4: '{}, {} and {others} others like this'
    # }[min(4, n)].format(*names[:3], others=n-2)

    # Trying to use compact syntax #############################################
    # Using dictionaries
    n = len(names)

    # # Create dictionary of string lenght and return string options
    likesStr =  {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }
    
    # Formats output string using data from input string
    # likesStr[min(4, n)] selects output string from dictionary
    # .format(*names[:3], others=n-2) replaces string arguments with values
    # If 4 names or more it uses first 2 names (*names) and cont of rest (others)
    print (likesStr[min(4, n)].format(*names[:3], others=n-2))

  
    # Old-school syntax #############################################    
    # likesStr = str()
    
    # if len(names) == 0:
    #     likesStr = "no one likes this"
    # elif len(names) == 1:
    #     likesStr = names[0] + " likes this"
    # elif len(names) == 2:
    #     likesStr = names[0] + " and " + names[1] + " like this"
    # elif len(names) == 3:
    #     likesStr = names[0] + ", " + names[1] + " and " + names[2] + " like this" 
    # else:
    #     likesStr = names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this"


    # print (likesStr)


likes([])
likes(['Peter'])
likes(['Jacob', 'Alex'])
likes(['Max', 'John', 'Mark'])
likes(['Daniel', 'Natalia', 'Alex', 'Jacob', 'Mark', 'Max'])