def solicitarDato(mensaje):
    """
        Esta funcion solicita un valor al usuario y retorna ese valor
        @param mensaje:String Cadena de texto que se le muestra al usuario
        @return int Retorna el valor que ingreso el usuario
    """
    return int(input(mensaje))

def invertirNumero(numero):
    """
        Esta funcion solicita un numero entero y lo retorna.
        @param numero:int valor para invertir.
        @return int numero invertido
    """
    n_inv = 0
    while numero > 0:
        n_inv = n_inv * 10 + (numero % 10)
        numero = numero // 10
    return n_inv

def contarDigitos(numero):
    """
        Esta funcion solicita un numero entero y cuanta sus digitos.
        @param numero:int valor para contar.
        @return int numero cantidad de digitos
    """
    cont_digitos = 1
    while numero > 9:
        cont_digitos += 1
        numero = numero // 10
    return cont_digitos

def dibujarNumeroEnFormatoDigital(numero, escala):
    """
        Esta funcion muestra en pantalla el numero ingresado en formato digital
        @param numero:int valor a mostrar
        @param escala:int el tamaño del numero
    """
    
    cont_pos = 0
    cont_repeticiones = 0
    while cont_pos < 5:
        dibujarLinea(numero, escala, cont_pos)
        if(cont_repeticiones < escala - 1 and (cont_pos == 1 or cont_pos == 3)):
            cont_repeticiones += 1
        else:
            cont_pos += 1
            cont_repeticiones = 0

def dibujarLinea(numero, escala, posicion):
    """
        Esta funcion dibuja la linea correspondiente de acuerdo a la posicion
        @param numero:int valor a mostrar
        @param escala:int el tamaño del numero
        @param posicion:int (0-4) 
            0: linea superior, 
            1: linea superior media
            2: linea media
            3: linea inferior media
            4: linea inferior
    """ 
    cont_digitos = contarDigitos(numero)
    cont = 0
    while cont < cont_digitos:
        res = (numero % 10)
        numero = numero // 10
        if posicion == 0:
            dibujarLineaSuperior(res, escala)
        if posicion == 1:
            if res == 0 or res == 4 or res == 8 or res == 9:
                print("|", end="")
                cont_repeticiones_horizontales = 0
                while cont_repeticiones_horizontales < escala:
                    print(" ", end="")
                    cont_repeticiones_horizontales += 1
                print("|", end="")
            elif res == 5 or res == 6:
                print("|", end="")
                cont_repeticiones_horizontales = 0
                while cont_repeticiones_horizontales < escala:
                    print(" ", end="")
                    cont_repeticiones_horizontales += 1
                print(" ", end="")
            else:
                print(" ", end="")
                cont_repeticiones_horizontales = 0
                while cont_repeticiones_horizontales < escala:
                    print(" ", end="")
                    cont_repeticiones_horizontales += 1
                print("|", end="")
        if posicion == 2:
            if res == 0 or res == 1 or res == 7:
                print(" ", end="")
                cont_repeticiones_horizontales = 0
                while cont_repeticiones_horizontales < escala:
                    print(" ", end="")
                    cont_repeticiones_horizontales += 1
                print(" ", end="")
            else:
                print(" ", end="")
                cont_repeticiones_horizontales = 0
                while cont_repeticiones_horizontales < escala:
                    print("-", end="")
                    cont_repeticiones_horizontales += 1
                print(" ", end="")
        if posicion == 3:
            if res == 0 or res == 6 or res == 8:
                print("|", end="")
                cont_repeticiones_horizontales = 0
                while cont_repeticiones_horizontales < escala:
                    print(" ", end="")
                    cont_repeticiones_horizontales += 1
                print("|", end="")
            elif res == 2:
                print("|", end="")
                cont_repeticiones_horizontales = 0
                while cont_repeticiones_horizontales < escala:
                    print(" ", end="")
                    cont_repeticiones_horizontales += 1
                print(" ", end="")
            else:
                print(" ", end="")
                cont_repeticiones_horizontales = 0
                while cont_repeticiones_horizontales < escala:
                    print(" ", end="")
                    cont_repeticiones_horizontales += 1
                print("|", end="")
        if posicion == 4:
            if res == 1 or res == 4 or res == 7:
                print(" ", end="")
                cont_repeticiones_horizontales = 0
                while cont_repeticiones_horizontales < escala:
                    print(" ", end="")
                    cont_repeticiones_horizontales += 1
                print(" ", end="")
            else:
                print(" ", end="")
                cont_repeticiones_horizontales = 0
                while cont_repeticiones_horizontales < escala:
                    print("-", end="")
                    cont_repeticiones_horizontales += 1
                print(" ", end="")
        cont += 1
    print("")

def dibujarLineaSuperior(digito, escala):
    """
        Funcion que dibuja la linea superior
        @param digito:int valor a dibujar
        @param escala:int tamaño de digito
    """
    if digito == 1 or digito == 4:
        print(" ", end="")
        cont_repeticiones_horizontales = 0
        while cont_repeticiones_horizontales < escala:
            print(" ", end="")
            cont_repeticiones_horizontales += 1
        print(" ", end="")
    else:
        print(" ", end="")
        cont_repeticiones_horizontales = 0
        while cont_repeticiones_horizontales < escala:
            print("-", end="")
            cont_repeticiones_horizontales += 1
        print(" ", end="")
def main():
    n = solicitarDato("Ingrese el numero n: ")
    escala = solicitarDato("Ingrese la escala: ")
    n_inv = invertirNumero(n)
    dibujarNumeroEnFormatoDigital(n_inv, escala)
    
main()