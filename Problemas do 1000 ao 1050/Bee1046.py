HoradeInicio,HoradeFim=list(map(int,input().split()))
if(HoradeInicio<HoradeFim):
    Tempo=HoradeFim-HoradeInicio
else:
    Tempo=HoradeFim+24-HoradeInicio
print(f"O JOGO DUROU {Tempo} HORA(S)")
    