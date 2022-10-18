from sys import stdin

def solicitarDato():
    """
        Solicita los datos al usuario separados por un espacio
        @return list/string contiene los valores del usuario la primera posicion es el tamaño
    """
    linea = stdin.readline().strip()
    if linea == "":
        return linea
    return [int(x) for x in linea.split(" ")]

def descrypt(datos):
    tam = datos[0]
    pos = 1
    while pos < tam:
        letra = chr(datos[pos] + 5)
        print(letra, end="")
        pos+=1

def main():
    while True:
        datos = solicitarDato()
        if datos == "":
            break
        descrypt(datos)
main()