def duplicate_count(s):
  #*** Master Solution
  # return len([c for c in set(s.lower()) if s.lower().count(c)>1])

  #*** LEARNING ABOUT SETS
  print("Input String:", s, "\n")
  #*** Manual definition of set using {}  
  #*** Only prints unique items. Since sets are not indexed, there is no way of knowing wich instance of duplicate item is being called  
  # thisset = {"apple", "banana", "cherry", "apple2", "kiwi", "cherry"}

  #*** Using {} assigns string as an element of set
  #*** Since used {} to define set the whole string is saved as 1 item in set and is printed here
  # thisset = {s}
  
  #*** Not using {} assigns each character of string as an entry in set
  #*** Each character is printed individualy including duplicates
  # thisset = s
  
  
  #*** Using set() constructor
  #*** Only prints case-sensitive unique items
  # thisset = set(s)

  #*** Using set() constructor and lower()
  #*** Only prints case-insensitive unique items
  #*** Dupluicate items are still saved  in set and can be counted (?) but are not printed.
  thisset = set(s.lower())
  
  # print(thisset)
  # for c in thisset:
  #       print (c) 

  dupChar = 0
  print("Set Definition: ", thisset, "\n")

  for c in thisset:
        if s.lower().count(c) > 1:
              dupChar = dupChar + 1
              # print ("Character", c, "repeats", s.lower().count(c), "times")
  
  print(dupChar)
          

  







#*** Test code:
duplicate_count("Indivisibilities")

# print (duplicate_count("Indivisibilities"))
# test.assert_equals(duplicate_count("aabbcde"), 2)
# test.assert_equals(duplicate_count("aabBcde"), 2)
# test.assert_equals(duplicate_count("indivisibility"), 1)
# test.assert_equals(duplicate_count("Indivisibilities"), 2)
# test.assert_equals(duplicate_count("aA11"), 2)
# test.assert_equals(duplicate_count("ABBA"), 2)

