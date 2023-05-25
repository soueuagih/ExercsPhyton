print("LOJINHA.")
print("Você ainda está devendo algumas parcelas do seu novo celular!")

val = float(input("Quanto foi o valor total do aparelho?"))
par = int(input("O pagamento será feito em quantas vezes?"))

p = val//par

print("\n")
print("Então são %a reais ao mês, por "%p ,par," meses.")

quant = int(input("Quantas parcelas faltam para terminar o pagamento?"))

rest = quant*p
jur1 = p*0.1
preco_comjuros = p + jur1

desc = preco_comjuros-(preco_comjuros*0.1)

total = quant*desc
preju2 = val - total

print("O valor restante a ser pago é de %f reais" %total)
print(" \n O vendedor terá %u reais de prejuízo." %preju2 )




