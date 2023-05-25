print("Precisamos de 3 medidas para compor os 3 lados do triângulo. ")
a = int(input("Lado A: "))
b = int(input("Lado B: "))
c = int(input("Lado C: "))

if (b-c)<a<(b+c) and (a-c)<b<(a+c) and (a-b)<c<(a+b):
    if (a == b and b==a) or (b==c and c==b) or (c==a and a==c):
        print("O triângulo é equilátero, pois todas as medidas informadas são iguais!")

    elif (a==b and b==a) or (b==c and b==a) or (c==a and c==b):
        print("O triângulo é isóceles, pois duas das medidas informadas são iguais!")

    elif (a!=b and a!=c) or (b!=c and b!=a) or (c!=a and c!=b):
        print("O triângulo é escaleno, pois duas das medidas informadas são iguais!")

    
else:
    print("Não é possível montar um triângulo válido com essas medidas!")


