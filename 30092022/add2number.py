from sys import stdin

def main():
    a = int(stdin.readline().strip())
    b = int(stdin.readline().strip())

    if a < 0 and b < 0:
        print("(" + str(a) + ")+(" + str(b) + ")=" + str(a + b))
    elif a < 0:
        print("(" + str(a) + ")+" + str(b) + "=" + str(a + b))
    elif b < 0:
        print(str(a) + "+(" + str(b) + ")=" + str(a + b))
    else:
        print(str(a) + "+" + str(b) + "=" + str(a+b))

main()