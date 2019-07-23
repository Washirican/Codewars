def count_smileys(arr):    
#In work
    numOfSmileys = 0
    for i in arr:
        if i.startswith(":") == True or i.startswith(";") == True:
            print (len(i))
            if i.endswith("D") == True or i.endswith(")") == True:
                numOfSmileys += 1

    print (numOfSmileys)


# return #the number of valid smiley faces in array/list

# count_smileys([';]', ':[', ';*', ':$', ';-D'])
count_smileys([':D',':~)',';~D',':)'])