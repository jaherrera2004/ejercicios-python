palabra = input("Introduce una palabra: ")
palabra_reverse = "".join(reversed(palabra))

if palabra == palabra_reverse:
    print("Es palíndromo")
else:
    print("No es palíndromo")