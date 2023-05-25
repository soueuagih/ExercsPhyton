print("Cálculo do peso ideal!")

s = str(input("Informe o sexo (M|F): "))
h = float(input("Altura: "))

if s.lower() == 'm':
    p = (72.7*h)-58
    print("O peso ideal é de ",p," kg.")

elif s.lower() == 'f':
    p = (62.1*h)-44.7
    print("O peso ideal é de ",p," kg.")
