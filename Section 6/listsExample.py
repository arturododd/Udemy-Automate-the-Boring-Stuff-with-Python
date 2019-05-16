# Section 6 Lists

#You make a list by placing values inside square brackets []
#And are comma-delimited meaning they are separated by commas

list1 = [1,2,3]
print(list1)

list2 = ['cat', 'bat', 'rat', 'elephant']
print(list2)

#In order to get individual values from a list
#you need to add the index of the value inside [] after the variable name
#In python the indexing starts at 0 and not at 1
#meaning the first value in a list will be index 0

print(list2[2]) #You want to know the value inside the list on the 3rd index

#You can even concatenate values inside a list for a print statement

print('The ' + list2[3] + ' is scared of the ' + list2[1])

#Lists can be contained inside other lists

list3 = [['cat', 'bat', 'rat', 'elephant'], [10,20,30,40,50]]
print(list3)

#If you want to get the value of one of the lists
#you use the same method but this time, use another index to select the list

print(list3[0][3]) #This is calling the first list and inside that list, the 4th value
print(list3[1][4]) #

