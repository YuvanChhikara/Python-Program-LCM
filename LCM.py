x=int(input("Enter first number: ")) #User input command
y=int(input("Enter second number: "))
z=x*y+1 
if x > y: #Finding the greater number is important
  greater = x
else:
  greater = y
  
while greater in range(1,z): #LCM can't be greater than the product of the numbers
 if (greater%x==0) and (greater%y==0): #Both numbers must divide it perfectly
    lcm=greater #Change the value of greater to LCM
    print(lcm)
    break #If we don't break the loop, it will turn into an infinite loop
 else:
    greater+=1 #We are incrementing the value of greater by 1. greater+=1 means greater=greater+1
