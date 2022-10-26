def fib(numero:int, memoria:list)->int:
    if len(memoria) <= numero:
        memoria.insert(numero, fib(numero - 2, memoria) + fib(numero - 1, memoria))
    return memoria[numero]

def fibNumeroGrandes(numero:int, memoria:list)->int:
    resultado = 0
    for i in range(numero // 500):
        fib(500*(i+1), memoria)
    return fib(numero, memoria)
    
def main():
memoria =[0, 1]
    print("fib(500)="+str(fib(500, memoria)))
    print("fib(1000)="+str(fib(1000, memoria)))
    print("fib(1500)="+str(fib(1500, memoria)))
    print("fib(2000)="+str(fib(2000, memoria)))
    print("fib(2500)="+str(fib(2500, memoria)))
    print("fibNumeroGrandes(20000)="+str(fibNumeroGrandes(20000, memoria)))

main()

