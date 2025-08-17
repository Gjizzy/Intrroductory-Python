#Create the Function
def validation(a,b):
    #If -else statements
    if a<0:
         print("Whoooa! Negative numbers are not allowed!")
    elif b<0:
         print("whoooaaa! ")
    if a==b:
        print("They're the same!")
    else:
        print("They're differnat!")


        a = int(input("Enter the 1st value: "))
        b = int(input("Enter the 2nd value: "))
                
                #Calling the function
                validation(a,b)