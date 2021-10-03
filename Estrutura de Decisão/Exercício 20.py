#    Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#    A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota1 = float(input('Insira a primeira nota do aluno: '))
nota2 = float(input('Insira a segunda nota do aluno: '))
nota3 = float(input('Insira a terceira nota do aluno: '))

media = (nota1 + nota2 + nota3) / 3

if media == 10:
    print('Aprovado com distinção, média 10.')
elif media < 7 and media >= 0:
    print('Reprovado, média %.2f.'%(media))
elif media > 7 and media < 10:
    print('Aprovado, média %.2f.'%(media))
else:
    print('Verifique os valores informados!')