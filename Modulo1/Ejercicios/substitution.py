import string
alfabeto = string.ascii_uppercase
clave= 'VCHPRZGJNTLSKFBDQWAXEUYMOI'
clave = clave.upper()
plaintext = input('introduzca palabra a encriptar: ')
ciphertext = ''
for letra in plaintext:
    index_alfa = alfabeto.find(letra.upper())
    
    if index_alfa >= 0:
        if letra.isupper():
            letra = clave[index_alfa]
        else:
            letra = clave[index_alfa].lower()
    ciphertext += letra
    
print('El texto codificado es: {}'format.ciphertext)
