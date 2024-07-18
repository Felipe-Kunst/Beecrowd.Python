TotalNotas = 0
SomaNotas = 0

while True:
    try:
        if TotalNotas == 2:
            break        
        nota = float(input())
        if 0 <= nota <= 10:
            TotalNotas += 1
            SomaNotas += nota
        else:
            print("nota invalida")
    except EOFError:
        break
Media = SomaNotas / 2.00

print("media = %0.2f" % Media)
