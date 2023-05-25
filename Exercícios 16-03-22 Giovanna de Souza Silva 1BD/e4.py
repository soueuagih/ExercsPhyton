print("Centro automotivo. Favor fornecer informações sobre o abastecimento de seu carro: ")
km_percorrid = float(input("Quantos quilometros você percorreu até aqui?"))
litros_abs = float(input("Quantos litros de combustível você usou? "))
cap_tanque = float(input("Qual a capacidade do seu tanque? "))

consumo = km_percorrid//litros_abs

print("A média de consumo de litros do seu carro é de: %s km/l" %consumo)
litrfalt = float(input("Quantos litros ainda restam no seu tanque? "))


falt = float(input("Quantos km ainda faltam até chegar ao seu destino? "))
falt2 = falt//consumo
r = litrfalt - falt2

if falt2 <= litrfalt:
        print("Tranquilo, você chegará ao seu destino sem precisar reabastecer o carro.")
else:
        print("Sugiro que passe em um posto logo. O carro precisará de reabastecimento.")
        print("Faltam %f litros" %r)
        
