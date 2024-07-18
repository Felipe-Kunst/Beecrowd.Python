Salario = float(input())

if(Salario > 0 and Salario <= 2000):
 print(f"Isento")
elif(Salario > 2000 and Salario <= 3000):
 resto = Salario - 2000
 resultado = resto * 0.08
 print(f"R$ {resultado:0.2f}")
elif(Salario > 3000 and Salario < 4500):
 resto = Salario - 3000
 resultado = (resto * 0.18) + (1000 * 0.08)
 print(f"R$ {resultado:0.2f}")
else:
 resto = Salario - 4500
 resultado = (resto * 0.28) + (1500 * 0.18) + (1000 * 0.08)
 print(f"R$ {resultado:0.2f}")