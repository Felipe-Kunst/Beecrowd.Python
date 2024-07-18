HoraInicial,MinutoInicial,HoraFinal,MinutoFinal = list(map(int,input().split()))

Diferenca = ((HoraFinal * 60) + MinutoFinal ) - ((HoraInicial * 60) + MinutoInicial)

if(Diferenca <= 0):
    Diferenca += 24*60
    
Hora = Diferenca//60
Minuto = Diferenca%60

print(f"O JOGO DUROU {Hora} HORA(S) E {Minuto} MINUTO(S)")