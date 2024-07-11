#!/usr/bin/env python
# coding: utf-8

# In[18]:


#Dictionaries in Python


# In[19]:


Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict)


# In[20]:


Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)


# In[21]:


Dict = {}
print("Empty Dictionary: ")
print(Dict)
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)

Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)
Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print("\nAdding a Nested Key: ")
print(Dict)


# In[22]:


Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

print("Accessing a element using get:")
print(Dict.get(3))



# In[23]:


dict = {
"country" : "India",
"continent" : "Asia",
"Other_name" : "Bharat"
}
x = dict["continent"]
print(x)


# In[24]:


#dictionary length
# A nested dictionary
dict2 = { # outer dictionary
	'Name': 'Steve',
	'Age': 30,
	'Designation': 'Programmer',
	'address': { # inner dictionary
		'Street': 'Brigade Road',
		'City': 'Bangalore',
		'Country': 'India'
	}
}
print("len() method :", len(dict2))
print("len() method with keys() :", len(dict2.keys()))
print("len() method with values():", len(dict2.values()))


# In[25]:


thisdict = {
    "brand" :"ford",
    "model"  :"mustang",
    "year"  : 1964 ,
}
x = thisdict.get("year")
print(x)

thisdict = {
    "brand" :"ford",
    "model"  :"mustang",
    "year"  : 1964 ,
}
x = thisdict.get("model")
print(x)


thisdict = {
    "brand" :"ford",
    "model"  :"mustang",
    "year"  : 1964 ,
}
x = thisdict.get("brand")
print(x)


# In[26]:


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

print(x)


# In[27]:


#values
# numerical values
dictionary = {"raj": 2, "striver": 3, "vikram": 4}
print(dictionary.values())


# string values
dictionary = {"geeks": "5", "for": "3", "Geeks": "5"}
print(dictionary.values())



# In[28]:


#items
# Python program to show working 
# of items() method in Dictionary 

# Dictionary with three items 
Dictionary1 = { 'A': 'Geeks', 'B': 4, 'C': 'Geeks' } 

print("Original Dictionary items:") 

items = Dictionary1.items() 

# Printing all the items of the Dictionary 
print(items) 

# Delete an item from dictionary 
del[Dictionary1['C']] 
print('Updated Dictionary:') 
print(items) 



# In[29]:


#popitem
# Python 3 code to demonstrate
# application of popitem()

# initializing dictionary
test_dict = {"Nikhil": 7, "Akshat": 1, "Akash": 2}

# Printing initial dict
print("The dictionary before deletion : " + str(test_dict))

n = len(test_dict)

# using popitem to assign ranks
for i in range(0, n):
	print("Rank " + str(i + 1) + " " + str(test_dict.popitem()))

# Printing end dict
print("The dictionary after deletion : " + str(test_dict))



# In[30]:


#update
# Python program to show working
# of update() method in Dictionary

# Dictionary with single item
Dictionary1 = {'A': 'Geeks'}

# Dictionary before Updation
print("Original Dictionary:")
print(Dictionary1)

# update the Dictionary with iterable
Dictionary1.update(B='For', C='Geeks')
print("Dictionary after updation:")
print(Dictionary1)



# In[ ]:




