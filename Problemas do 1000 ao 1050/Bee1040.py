Nota1,Nota2,Nota3,Nota4 = map(float,input().split())
Media = ((Nota1 *2) + (Nota2 * 3) + (Nota3 * 4) + Nota4 )/10
print(f'Media: {Media:.1f}')
if(Media >= 7):
    print('Aluno aprovado.')
elif(Media < 4.9):
    print('Aluno reprovado.')
elif( Media >=5 and Media < 7.0):
    print('Aluno em exame.')
    NotaExame = float(input())
    print(f'Nota do exame: {NotaExame:.1f}')
    MediaFinal = (Media + NotaExame)/2
    if (MediaFinal >= 5.0):
        print('Aluno aprovado.')
        print(f'Media final: {MediaFinal:.1f}')
    elif(MediaFinal < 5.0):
        print('Aluno reprovado.')
        print(f'Media final: {MediaFinal:.1f}')