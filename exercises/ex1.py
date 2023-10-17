#Exercise 1: Write a function, add_it_up(), that takes a single integer as input and 
#returns the sum of the integers from zero to the input parameter.

#def add_it_up(number):
#    num = 1
#    summation = 0
#    while num < number + 1:
#        summation = summation + num
#        num = num + 1
#    return(summation)

def add_it_up(number):
    summation = 0
    for add in range(1, number+1):
        summation = summation + add
    return summation

print("Sum of a range of integers")

while  1 == 1:

    try:
        number = int(input("Enter a number: "))

        while number <= 0:
    
            print("Enter an integer greater than 0")
            number = int(input("Enter a number: "))

        print(add_it_up(number))

    except ValueError:
        print("Enter only integers plz")



