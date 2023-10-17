def modifyString(input_str):
    new_string = ""
    
    for char in input_str:
        if char not in new_string:
            new_string += char

    print(new_string)

input_str = str(input("Introduce un string: "))
modifyString(input_str)
