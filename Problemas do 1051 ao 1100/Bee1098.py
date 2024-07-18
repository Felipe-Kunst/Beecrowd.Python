i = 0
j = 1
Valor = 0
Count = 0
Control = 0

while (i <= 2):
    if (Control == 0):
        print("I=%.0f J=%.0f" % (i, j))
    else:
        print("I=%.1f J=%.1f" % (i, j))
    Count += 1
    
    if (Count == 3):
        i += 0.2
        Valor += 0.2
        j = Valor
        Count = 0
        Control += 1

    if(Control == 5):
        Control = 0
    j += 1