while True:
    SomaNotas = 0
    NotasValidas = 0
    
    while NotasValidas < 2:
        nota = float(input())
        
        if 0 <= nota <= 10:
            SomaNotas += nota
            NotasValidas += 1
        else:
            print("nota invalida")
    
    media = SomaNotas / 2
    print("media = %.2f" % media)
    
    while True:
        print("novo calculo (1-sim 2-nao)")
        novo_calculo = int(input())
        
        if novo_calculo in [1, 2]:
            break
    
    if novo_calculo == 2:
        break
