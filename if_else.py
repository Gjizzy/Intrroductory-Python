#If else statements
#Execute some logic or instructions if (and only If) the condition it's correct
#We can catch with an else in case that the condition doesn't match
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Greater than: a <= b
age = 22

if age < 100: 
  if age < 21: 
    print("You're a minor without access!")
  else: 
    print("You're younger than a 100 year old")
elif age==100:
  print("Congartulations, you got to live a acentury!")
else:
  print("Sorry, you're getting old!")

  #Exercise
  x = 8
  y = 8
  if x > y:
    print("Hello")
  else:
    print("Welcome")

x = "Hello"
y = "hello" 

if x == y:
  print("It's the same world")
else:
  print("They're differant")