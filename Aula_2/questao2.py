salario = int(input("salario:"))
imposto = input("Imposto:")

if not imposto:
    imposto = 27.5
else:
    imposto = float("imposto")
sal = salario - (salario * (imposto * 0.01))
print(sal)
