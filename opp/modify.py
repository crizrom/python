
def modifyString(input_str):
    new_string = ""
    for xhar in range(len(input_str)):
        contador = 0
        zhar = xhar
        #new_string = ""
        for zhar in range(xhar, len(input_str)):
        #for zhar in range(xhar, len(input_str)):
            #contador = 0
            if input_str[zhar] == input_str[xhar] and contador == 0:
                contador += 1 #aqui
                new_string = new_string + input_str[xhar]

            elif input_str[zhar] == input_str[xhar] and contador >= 1:
                new_string = new_string
    print(new_string)
        #print(input_str[xhar], end = "")
        

input_str = str(input("Introudce un string: "))
modifyString(input_str)
print(" ")




def modifyString(input_str):
    new_string = ""
    
    for char in input_str:
        if char not in new_string:
            new_string += char

    print(new_string)

input_str = str(input("Introduce un string: "))
modifyString(input_str)
