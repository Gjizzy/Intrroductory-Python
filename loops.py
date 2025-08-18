#For loops
#Is used for iterating over a sequence (list, tuples, dictionaries, set, strings)
#keywords: continue - jumps to the next iterations and break 
fruits_list = ["apple","banana","cherry", "orange", "banana",]

my_dictionary = {
    "brand":"Ford",
    "model":"Mustang",
    "year" :"1964",
    "colors" :["red","white","blue","black"]
}
    
for fruit in fruits_list:
    if fruit== "cherry":
    #break
    continue
    print(fruit)

    print("------------------------")

    for items in my_dictionary:
    print(f"keys onl: {items} Retreiving the value: {my_dictionary[items]}")
    
    print("-----------------")

    for x in "iteration":
        print(x)


        print("-----------------------" 
              

    # range(START_VALUE, STEPS OR INCREMENTS)
        "for number in range(0,len(fruits_list),2):
        print(fruits_list[number])







