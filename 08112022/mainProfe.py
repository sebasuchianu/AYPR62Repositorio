from sys import stdin
def solicitarDato():
    return stdin.readline().strip()
    
def main():
    while True:
        palabra = solicitarDato()
        palabra2 = solicitarDato()
        if palabra == "" or palabra2 == "":
            break
        letras = []
        for letra in palabra:
            if letra in palabra2:
                letras += letra
                palabra2 = list(palabra2)
                palabra2.remove(letra)
                palabra2 = "".join(palabra2)
        letras.sort()
        print("".join(letras))
        
main()