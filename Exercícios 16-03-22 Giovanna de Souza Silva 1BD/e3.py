print("Programa de inversão de números...")

num = int(input("Digite um número de 3 dígitos: "))

i = 0

while(num != 0):
    temp = num % 10
    inverso = inverso * 10 + temp
    num = num // 10

print("O valor invertido é:", i)
