nome=str(input())
salario=float(input())
total=float(input())
comissao=total*15/100
montante=salario+comissao
print(f'TOTAL = R$ {montante:.2f}')