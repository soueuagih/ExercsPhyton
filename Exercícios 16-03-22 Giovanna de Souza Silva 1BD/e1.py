print("Vamos calcular média ponderada!")
n1 = float(input("Por favor, digite o primeiro número:"))
n2 = float(input("Por favor, digite o segundo número:"))
n3 = float(input("Por favor, digite o terceiro número:"))
n4 = float(input("Por favor, digite o quarto número:"))
n5 = float(input("Por favor, digite o quinto número:"))

m = (n1*0.3)+(n2*0.3)+(n3*0.3)+(n4*0.2)+(n5*0.2)/(0.3+0.3+0.3+0.2+0.2)

print("A média ponderada é de: %s" %m)
