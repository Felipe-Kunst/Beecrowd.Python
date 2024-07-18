X =int(input())
Horas = X//60**2
X= X - Horas *60**2
Minutos = X//60
X= X - Minutos*60
Segundos = X
print('{}:{}:{}'.format(Horas, Minutos, Segundos))