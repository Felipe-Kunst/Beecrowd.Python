Tempo = int(input())
Anos = Tempo//365
Tempo = Tempo - Anos*365
Mes= Tempo //30
Tempo= Tempo-Mes*30
Dias = Tempo
print('{} ano(s)'.format(Anos))
print('{} mes(es)'.format(Mes))
print('{} dia(s)'.format(Dias))
