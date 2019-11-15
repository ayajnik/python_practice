print('---------------------------------------------------------------------------------------------------------------------------SESSION - 1-----------------------------------------------------------------------------------------------------------------------')
print('\n')
print('Practicing Lists and List Comprehension')
print('\n')
print('''The structure for list comprehension is as follows -->> [result, for loop, conditional syntax]''')
print('\n')

##converting a dictionary to a list
my_dict = {'a':1, 'b':2,'c':3,'d':4}
a = list(my_dict.values())
f = list(my_dict.keys())
print("The values obtained from the dictionary's values are :  ", a)
print("The items obtained from the dictionary's keys are :  ", f)
##extend() -->> extending a current list with another list, either i used a + b

b = [5,6,7,8,9]
new = a + b
print('The new list is as follows : ', new)
b_1 = [10,11,12,13,14]
a.extend(b_1)
print(a)
## insert(x,y) -->> inserting a value at a particular where x represents the position where we have to insert the value and y represents the value

c = 'ayush'
new.insert(1,'ayush is a goood bwooyyy')
print(new)


##remove()
print('We need to remove the string from the list we are dealing with and hence the final list is as follows ', new.remove('ayush is a goood bwooyyy'))

##sort()
new.sort()
print(new)
new.sort(reverse=True)
print(new)
new_1 = new + b_1
print(new_1)
print(new_1[0:-1:2])

