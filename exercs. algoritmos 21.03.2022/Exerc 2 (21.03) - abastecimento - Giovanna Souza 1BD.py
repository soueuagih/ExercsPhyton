print("Abastecimento do veículo!")
tipo = str(input("Informe o tipo de combustível desejado (A- álcool, G- gasolina :)"))
print("Lembrando que o preço do litro da gasolina é 3,30 reais; e o do álcool é 2,90 reais.")
ltr = int(input("Quantos litros você vai colocar? )"))

if tipo.lower() == 'a':
    if ltr <= 20:
    conta = (3.30 -(3.30*0.03))*ltr
        print("O valor a ser pago é de %d reais." %conta)

    else:
        conta = (3.30 -(3.30*0.05))*ltr
        print("O valor a ser pago é de %d reais." %conta)


if tipo.lower() == 'g':
    if ltr <= 20:
    conta = (2.90 -(2.90*0.04))*ltr
        print("O valor a ser pago é de %d reais." %conta)

    else:
        conta = (2.90 -(2.90*0.05))*ltr
        print("O valor a ser pago é de %d reais." %conta)
