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

def generarVectorDiferencias(datos):
    """
        Funcion que genera la diferencia absoluta entre elementos sucesivos
        @param datos:list son todos los datos ingresado por el usuario la primera posicion debe ser el cantidad de datos
        @return list una lista de las diferencias y la primera posicion es el tamaño.
    """
    tam = datos[0]
    diff = [int(0) for _ in range(tam)]
    diff[0] = tam - 1
    pos = 1
    while pos < tam:
        resta = datos[pos] - datos[pos+1]
        if resta < 0:
            resta *= -1
        diff[pos] = resta
        pos+=1
    return diff

def buscarSecuencia(diff):
    """
        Funcion que busca si es jolly o no jolly
        @param diff:list valores a comparar
        @return boolean True si es Jolly False si no lo es
    """
    tam = diff[0]
    buscar = 1
    while buscar <= tam:
        encontre = False
        pos = 1
        while pos <= tam:
            if diff[pos] == buscar:
                encontre = True
            pos+=1
        if encontre == True:
            buscar +=1
        else:
            buscar = tam + 1 
    return encontre

def main():
    while True:
        datos = solicitarDato()
        if datos == "":
            break
        diff = generarVectorDiferencias(datos)
        if buscarSecuencia(diff):
            print("Jolly")
        else:
            print("Not Jolly")
main()