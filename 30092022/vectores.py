from sys import stdin
def ingresarNumeroEntero(mensaje):
    """
        Esta funcion solicita un valor entero al usuario
        @param mensaje:string Variables donde se envia el mensaje que se va a mostrar al usuario
        @return int valor capturado por el usuario
    """
    print(mensaje)
    return int(stdin.readline().strip())

def solicitarNotas(cantidad):
    """
        Esta funcion solicita las notas al usuario
        @param cantidad:int cantidad de notas que se le solicita al usuario
        @return list retorna todas las notas ingresadas por el usuario
    """
    print("Ingrese cada nota: ")
    return [int(stdin.readline().strip()) for _ in range(cantidad)]

def promedioNotas(notas, cantidad):
    """
        Esta funcion calcula el promedio
        @param notas:list Todas las notas a promediar
        @param cantidad:int La cantidad de notas que tiene la variable notas
        @return float El promedio de las notas
    """
    pos = 0
    promedio = 0
    while pos < cantidad:
        promedio += notas[pos]
        pos += 1
    return promedio/cantidad

def encontrarNotasMayoresAPromedio(notas, cantidad, promedio):
    """
        Esta funcion busca y visualiza las notas mayores al promedio
        @param notas:list Todas las notas a promediar
        @param cantidad:int La cantidad de notas que tiene la variable notas
        @param promedio:float promedio de notas
    """
    print("Valores superiores son: ", end="")
    pos = 0
    while pos < cantidad:
        if notas[pos] > promedio:
            print(notas[pos], end=" ")
        pos+= 1
        

def main():
    """
        esta funcion ejecutara otras funciones para resolver el problema
    """
    n = ingresarNumeroEntero("Ingrese cantidad de notas en formato entero: ")
    notas = solicitarNotas(n)
    promedio = promedioNotas(notas, n)
    print("promedio es: " + str(round(promedio, 2)))
    encontrarNotasMayoresAPromedio(notas, n, promedio)
main()

