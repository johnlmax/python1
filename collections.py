# a list in Python is a type of collection - there are many others
# lists are:
    # zero-indexed
    # modifiable in-place
    # may have duplicates

numbers = [2,4,6,8]
# accessing/getting:
print(numbers[0]) # 2
# mutating/setting
numbers[0] = 0
# adding
numbers.append(10) 
print(numbers) # 0,4,6,8,10
numbers.insert(3, 99)
print(numbers) #[0, 4, 6, 99, 8, 10] note indices above the inserted element change + 1

my_empty_list = []
my_empty_list.append("Amar")
my_empty_list.append("John")
my_empty_list.append("Alan")
my_empty_list.append("Fred")
my_names = my_empty_list
print(my_names)

my_names.append("Tina")
print(my_names) # ['Amar', 'John', 'Alan', 'Fred', 'Tina']
print(my_empty_list) # ['Amar', 'John', 'Alan', 'Fred', 'Tina']
# what is going on??
# there is ONLY ONE LIST
# line 23 my_names = my_empty_list is a SHALLOW COPY of the REFERENCE ONLY
# it doesn't make a new list
# fortunately, Python has tools to get round this
# in other languages, the immutable copying of complex datatypes is quite a throny issue
import copy
my_names_2 = copy.copy(my_empty_list)
my_names_2.append("Van Morrison")
print(my_names_2) #['Amar', 'John', 'Alan', 'Fred', 'Tina', 'Van Morrison']
print(my_empty_list)# ['Amar', 'John', 'Alan', 'Fred', 'Tina'] original unaffected

tina_turner = my_names_2[4]
print(tina_turner)

# deleting elements
del(my_names_2[3])
print(my_names_2)

# how to lookup builtins