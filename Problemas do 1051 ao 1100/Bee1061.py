dia,DataInicial=input().split()
DataInicial = int(DataInicial)
HoraInicial,MinutoInicial,SegundoInicial=map(int,input().split(":"))

dia,DataFinal=input().split()
DataFinal = int(DataFinal)
HoraFinal,MinutoFinal,SegundoFinal=map(int,input().split(":"))

Segundos = SegundoFinal - SegundoInicial
Minuto = MinutoFinal - MinutoInicial
Horas = HoraFinal - HoraInicial
Dias = DataFinal - DataInicial

if(Segundos<0):
	Segundos+=60
	Minuto-=1


if(Minuto<0):
	Minuto+=60
	Horas-=1

if(Horas<0):
	Horas+=24
	Dias-=1

print(f"{Dias} dia(s)")
print(f"{Horas} hora(s)")
print(f"{Minuto} minuto(s)")
print(f"{Segundos} segundo(s)")