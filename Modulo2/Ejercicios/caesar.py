import string
alfabeto = string.ascii_uppercase
clave= 'VCHPRZGJNTLSKFBDQWAXEUYMOI'
clave = clave.upper()

#LEEMOS PLAINTEXT
plaintext = input('introduzca palabra a encriptar: ')

ciphertext = ''
for letra in plaintext:
    
    # algoritmo transformacion
    index_alfa = alfabeto.find(letra.upper()) # posicion de letra en alfabeto
    
    if index_alfa >= 0:
        if letra.isupper():
            letra = clave[index_alfa] # transformo letra segun indice encontrado
        else:
            letra = clave[index_alfa].lower()
    # Completando 'ciphertext' : 'a' + 'b'
    ciphertext += letra
    
print('El texto codificado es: ' +ciphertext)
