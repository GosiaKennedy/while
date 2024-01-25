# program to contiunually ask the user to enter a number, to stop when the user enters'-1'  
# and to calculate the average of entered numbers 

total = 0
counter = 0 # control variable, each time the loop executes counter increases by 1 

number = int(input("Enter a number:")) # ask the user to input a number
while number != -1: # condition to specify when the loop will end
    counter += 1 # increases with every pass of the loop
    total += number # total equals total plus number entered by the user
    number = int(input("Enter a number:")) 

if counter == 0:
    counter = 1 # in case first number is -1, prevents division by zero 

print (f"The average of all numbers is {total/counter}") # average is equal to sum of all numbers (total) divided by amount of numbers


