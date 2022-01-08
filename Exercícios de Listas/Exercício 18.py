# Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo.
# Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos.
# Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação Python. Para computar cada voto, a
# telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero,
# indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem
# de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:

# O total de votos computados;
# Os númeos e respectivos votos de todos os jogadores que receberam votos;
# O percentual de votos de cada um destes jogadores;
# O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.

# Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador.
# O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função.
# Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e
# retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao
# exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes
# ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.

# Enquete: Quem foi o melhor jogador?

# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 11
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 50

# Informe um valor entre 1 e 23 ou 0 para sair!
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 0

# Resultado da votação:

# Foram computados 8 votos.

# Jogador Votos           %
# 9               4               50,0%
# 10              3               37,5%
# 11              1               12,5%
# O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.



# Estou trabalhando ainda neste código, ele está funcional porém precisa ser melhorado.

# Ainda falta:
#   * Colocar um espaçamento dinâmico no resultado, para que todo ele fique sempre alinhado
#   * Codificar para que quando houver empate o programa mostre os candidatos empatados
#   * Revisar

votos = []
print('Enquete: Quem foi o melhor jogador?')

while True:
  entrada = int(input('Número do jogador 1 a 23 (0=fim): ')) 

  if entrada == 0:
     break

  if entrada > 0 and entrada < 24:  
    votos.append(entrada)
    print()
  else:
    print('Entrada inválida')

print('Programa finalizado')

print('\nForam computados {} votos'.format(len(votos)))
print()


print('Jogador - Votos - Porcentagem')

melhorJogador = 0
votosMelhorJogador = 0

for i in range(23):
  x = votos.count(i+1)
  porcentagem = (x*100)/len(votos)

  if x > votosMelhorJogador:
    melhorJogador = i + 1 # número equivalente do Jogador
    votosMelhorJogador = x # qntd de votos   
    
  
  if porcentagem != 0:
    print('{}          {}'.format(i+1,x),end='')
    print('       {:.1f}%'.format(porcentagem))

print('O melhor jogador foi o número {}, com {} votos, correspondendo a {:.1f}% do total de votos'.format(melhorJogador,votosMelhorJogador,(votosMelhorJogador*100)/len(votos)))
