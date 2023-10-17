def eliminar_duplicados(cadena):
    caracteres_unicos = set()
    resultado = ""
    
    for caracter in cadena:
        if caracter not in caracteres_unicos:
            caracteres_unicos.add(caracter)
            resultado += caracter

    return resultado

entrada = "aabbcdeff"
salida = eliminar_duplicados(entrada)
print(salida)  # Esto imprimirá "abcdf"
