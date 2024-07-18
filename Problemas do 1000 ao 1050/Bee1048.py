Salario = float(input())
if(Salario>=0 and Salario<=400):
	Reajuste= Salario*0.15
	NovoSalario=Salario+Reajuste
	Percentual=15
elif(Salario>=400.01 and Salario<=800.00):
	Reajuste=Salario*0.12
	NovoSalario=Salario+Reajuste
	Percentual=12
elif(Salario>=800.01 and Salario<=1200.00):
    Reajuste=Salario*0.1
    NovoSalario=Salario+Reajuste
    Percentual=10
elif(Salario>=1200.01 and Salario<=2000.00):
	Reajuste=Salario*0.07
	NovoSalario=Salario+Reajuste
	Percentual=7
elif(Salario>2000):
	Reajuste=Salario*0.04
	NovoSalario=Salario+Reajuste
	Percentual=4
print(f"Novo salario: {NovoSalario:.2f}")
print(f"Reajuste ganho: {Reajuste:.2f}")
print(f"Em percentual: {Percentual} %")