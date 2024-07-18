while(True):
    try:
        Senha = int(input())
        if(Senha==2002):
            print("Acesso Permitido")
            break
        else:
            print("Senha Invalida")
    except EOFError:
        break