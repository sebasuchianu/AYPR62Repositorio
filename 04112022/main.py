M=[[int(0) for _ in range(4)] for _ in range(5)]
print(M)
M=[[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
print(M)
for fila in M:
  print(fila)
for fila in M:
  for elemento in fila:
    print(elemento, end=" ")
  print("")
a = "separador"
print(f"{a:*^50}")

for fila in M:
  print(" ".join([str(x) for x in fila]))

a = "separador"
print(f"{a:*^50}")
M=[[int(0) for _ in range(4)] for _ in range(5)]
print(M)
a = "separador"
print(f"{a:*^50}")
M=[]
for _ in range(5):
  temp = []
  for _ in range(4):
    temp.append(int(0))
  M.append(temp)
print(M)