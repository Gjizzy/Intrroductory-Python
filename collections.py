#Python collections
#A group of data elements in python that allows us to store multiple
#data in a single variable

#1. Lists - They're used to store multiple items ina single variable
#and they use square brackets
# Properties:
# Properties: lists are ordered, changeable (or mutable) and allow duplicates
empty_list = [] # this is an empty list
print(f"Collection Data type: {type(empty_list)}") #Data type

fruits_list = ["apple","banana","cherry", "orange", "banana",] 
#              0      1         2         3        4
print(f"Empty List: {empty_list}")
print(f"List: {fruits_list}")
print(f"Retreiving a valie: {fruits_list[0]}")
print(f"List length: {len(fruits_list)}")
print(f"Acessing Elements by Negative Indexing: {fruits_list[-1]}")
print(f"Accessing Elements by ranges[n:n]: {fruits_list[0.3]}")
# [a:b] where a is the starting index in the array (included) and b is the stopping point(excluded) from the list
print(f"Accessing Elemenst by ranges[:n]: {fruits_list[:2]}")
print(f"Accessing Elements by ranges [n: ]: {fruits_list[1:]}")
#Adding elements to the list
fruits_list.append("watermelon")
fruits_list.append("strawberry")
print(f"Adding elements: {fruits_list}")
#Remove elements from the list
fruits_list .pop(6)
fruits_list .pop()
print(f"Removing element from list: {fruits_list}")
fruits_list.remove()
fruits_list.insert(0,"pear")
print(fUsing insert method: {fruits_list}")
      fruits_list.clear()
      print(fruits_list)
      fruits_list[2] = "bluebery"
      print(f"Changing actual values: {fruits_list}")

      #2. Dictionar
      # my_dictionary.update({"year":})
      #Are used to storedat values in key:value pairs.
      #properties: ordered, changedable and do not allow duplicates
      my_dictionary = {
          "brand":"Ford",
          "model": "Mustang",
          "year".1964,
          "colors":["red", "white", "blue", "black"]
      }
      print(f"--------------Dictionaries--------------")
      print(f"Dictionary: {my_dictionary['year']}")
      print(f"Accessing items using keys: {my_dictionary['year']}")
      print(f"Dictionary length: {len(my_dictionary)}")
      print(f"Accessing items using get: {my_dictionary.keys()}")
      print(f"Only orint the keys: {my_dictionary.keys()}")
      print(f"Only print the values:{my_dictionary.values()}"
            # my_dictionary["year"] = 1984
            my_dictionary.update({"year":1985})
            print(f"Modifying the dictionary: {my_dictionary}")
            my_dictionary.pop("colors")
            print(f"Deleting elements: {my_dictionary}")
            
            #3. Tuples
            #Store multiple items in a single variable
            #Properties: ordered and unchangeable
            print(f"-----------------------Tuples--------------")
my_tuple = ("apple","banana", "cherry",)
print(f"Tuple: {my_tuple} Data Type: {type(my_tuple)}")
print(f"Accessing elements:{my_tuple[2]}")
modified_tuple.append("Watermelon")
modifies_tuple.pop(0)
my_tuple = tuple(modified_tuple)
print(f"Tuple: {my_tuple}  Data type:  {type(.my_tuple)}")

