print("Cálculo de idade!")
d = int(input("Informe, em números, o dia no qual você nasceu: "))
m = int(input("Agora, novamente em números, o mês: "))
a = int(input("Por último, o ano no qual você nasceu: "))


print("Obrigada!")
print("Agora por favor informe, em números...")
dh = int(input("Que dia é hoje: "))
mh = int(input("Em que mês estamos: "))
ah = int(input("Em que ano estamos: "))

calc_ano = (ah-a)
calc_mes = 12*calc_ano
calc_dia = 365*calc_ano

print("Ok!")
print("Calculando...")

print("Você tem %i anos..." %calc_ano)
print("%s meses..." %calc_mes)
print("e %g dias!..." %calc_dia)
