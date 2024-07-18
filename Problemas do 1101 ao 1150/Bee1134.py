alcool = 0
gasolina = 0
diesel = 0

while True:
    tipo = int(input())
    
    if tipo == 4:
        break
    elif tipo == 1:
        alcool += 1
    elif tipo == 2:
        gasolina += 1
    elif tipo == 3:
        diesel += 1
    else:
        continue  
print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")
