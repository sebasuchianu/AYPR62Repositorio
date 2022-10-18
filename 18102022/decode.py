def buscarLetra(letra, base64):
    pos = 0
    encontrado = False
    while pos < 64 and encontrado == False:
        if base64[pos] == letra:
            encontrado = True
        else:
            pos += 1
    return pos

def tamVector(datos):
    pos = 0
    try:
        while pos < 10000000000000000000000000000000000000000:
            a = datos[pos]
            pos+= 1
    except:
        return pos

def convertirBase64aBinario(datos):
    resultado = ""
    base64 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z',
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              '+', '/']
    binario = ["000000", "000001", "000010", "000011", "000100", "000101", "000110", "000111", 
               "001000", "001001", "001010", "001011", "001100", "001101", "001110", "001111",
               "010000", "010001", "010010", "010011", "010100", "010101", "010110", "010111",
               "011000", "011001", "011010", "011011", "011100", "011101", "011110", "011111",
               "100000", "100001", "100010", "100011", "100100", "100101", "100110", "100111", 
               "101000", "101001", "101010", "101011", "101100", "101101", "101110", "101111",
               "110000", "110001", "110010", "110011", "110100", "110101", "110110", "110111",
               "111000", "111001", "111010", "111011", "111100", "111101", "111110", "111111"]

    for letra in datos:
        if letra != "=":
            posEncontrada = buscarLetra(letra, base64) 
            resultado = resultado + binario[posEncontrada]
    return resultado

def main():
    test = "MDEyMw=="
    bin_test = convertirBase64aBinario(test)
    elementosAquitar = tamVector(bin_test) % 8
    print(elementosAquitar)

main()