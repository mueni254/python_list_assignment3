#create a list
my_list =[]
print(my_list)

# append elements to the list
my_list.append(10)  
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#3.	Insert the value 15 at the second position in the list.
my_list.insert(1,15)
print(my_list)

#4.	Extend my_list with another list: [50, 60, 70].
my_list.extend([50,60,70])
print(my_list)

#5.	Remove the last element from my_list
my_list.pop()
print(my_list)

#sort list in ascending order
my_list.sort()
print(my_list)

#7.	Find and print the index of the value 30 in my_list
print(my_list.index(30))


