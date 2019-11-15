print('--------------------------------------------------------------------------------------------------------------------------SESSION - 2------------------------------------------------------------------------------------------------------------------------')

print('\n')
print('Author: Ayush Yajnik')
print("Learning Python's Dictionary")
print('\n')

Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
  
# Creating a Dictionary  
# with Integer Keys 
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 
  
# Creating a Dictionary  
# with Mixed keys 
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 
  
# Creating a Dictionary 
# with dict() method 
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 
  
# Creating a Dictionary 
# with each item as a Pair 
Dict = dict([(1, 'Geeks'), (2, 'For')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 


# Creating a Nested Dictionary  
# as shown in the below image 
Dict = {1: 'Geeks', 2: 'For',  
        3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}} 
  
print(Dict)


##adding a value to the dictionary

Dict['ayush_yajnik'] = 'is learning python'
print(Dict)


##looping over a dictionary

statesandcapitals = {
     'Rajasthan' : 'Jaipur',
     'Uttar Pradesh' : 'Lucknow',
     'Haryana' : 'Chandigarh',
     'Punjab' : 'Chandigarh',
     'Bihar' : 'Patna'
     }

for states in statesandcapitals:
     print('The states we are dealing with are : ', states)


##maintaing the order of the list
#from Counter import OrderedDict

#statesandCapitals = OrderedDict(
#     [('Maharashtra' , 'Mumbai'),
#     ('Bengaluroo' ,'Karnataka'),
#     ('Goa', 'Panaji'),
#     ('Andhra Pradesh' 'Hyderabad'),
#     ('Kerela' , 'Thiruvanandapuram'),
#     ('Telangana', 'Amaravati'),
#     ('Tamil Nadu' , 'Chennai')])


#print('The Southern States of India are :')
#print('\n')
#for capitals in statesandCapitals:
#     print(capitals)


##printing keys and values
print('Printing both the keys and values in the dictinary ; ')
print('\n')
for keys, values in statesandcapitals.items():
     print(keys, ':', values)

