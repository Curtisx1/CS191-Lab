#initialize strings to use
string1 = "thisismylist"
string2 = "thisismyotherlist"
string3 = "thisismylastlist"
alpha = "abcdefghijklmnopqrstuvwxyz"

#Part1a:  create a list of EACH string. the first is provided
listString1 = [char for char in string1]


#Part1b:  add code to sort each list (list 1 is given)
listString1.sort()


#Part 1c:  code to get rid of duplicates from each list (list 1 is given) 
sortSet1 = list(dict.fromkeys(listString1))
sortSet2 = []


#Part 2a:  update this code code to find the union of these three lists 
#          hint: union is the 'sum' of the 3 sets
sortSetUnion = sortSet1 

#Part 2b:  add the code to sort this new set and get rid of duplicates
#          this is done for you
sortSetUnion = sorted(sortSetUnion)
sortSetUnion = list(dict.fromkeys(sortSetUnion))

#Part 2c: add additional code to print all 3 sets and the union 
print("1.   string1 set   = ", sortSet1)


print (" ")
print("2.   Union of sets = ", sortSetUnion)

print(' ')

#Part 3a: compute and print out the set set1(A) - set2(B)
#        outer loop goes through set1
#        if the element is not in set 2
#        add to the AminusB set & print the set
#        the first one is done for you
AminusB = set()
for element in sortSet1:         
    if not(element in sortSet2): 
        AminusB.add(element)     
      
print('3a.  string1 - string2 = ', sorted(AminusB))
print(' ')


#Part 3b: write the code to compute B-A
BminusA = set()
for element in sortSet2:         
    print ("replace this print with the code to do this")
      
print('3b.  string2 - string1 = ', sorted(BminusA))
print(' ')



#Part 3c: add the code to compute the symmetric difference of string1
#        string2.  NOTE: if you want to use earlier logic, 
#        you will need to change the set to a list using list(setName)
#        make sure to sort this set 

AsymdiffB = []

print('3c.  Symmetric Difference of string1 and string2 = ', sorted(AsymdiffB))
print(' ')

#Part 4: add code to compute the symmetric difference of string2 and string3
#        you will need to add code similar to AminusB, BminusA and AsymdiffB
#
BsymdiffC = set()






print('4.   Symmetric Difference of string2 and string3 = ', sorted(BsymdiffC))
print (' ')

#Part 5: using logic from AminusB, find the complement of string3
#        where the universal set is alpha
complC = set()
for element in alpha:
  print ("replace this print with the remaining logic needed to find the complement")




print ("5.   The complement of string3 = ", sorted(complC))
print (' ')

#Part 6:  find the intersection of these 3 lists
#         hint:  there is an intersection function in python
set1 = set(listString1)

result = []
print ("6.   The intersection = ", sorted(result))