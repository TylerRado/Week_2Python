my_list = [] # The empty list.

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(f'The Original list{my_list}')

my_list.insert(1,15)  # Inserting the value 15 at second position

print(f'list with the value "15".{my_list}')

my_second_list = [50,60,70]
my_list.extend(my_second_list)   # Extend list

print(f'Extended list.{my_list}')

my_list.remove(70)

print(f'Removing the last element in the list.{my_list}') # Remove element in the list

sort_myList = sorted(my_list)
print("Sorted list",sort_myList)  # my sorted list.

print("Indexing of the value",sort_myList[-4]) # Finding the value 30 in the list.




