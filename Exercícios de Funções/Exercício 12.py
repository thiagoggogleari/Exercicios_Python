# Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. 
# Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. 
# Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

def embaralha(palavra):
  lista = []
  resposta = ''
  
  # Coloca as letras em um array
  for i in range(len(palavra)):
    lista.append(palavra[i])
  
  # Embaralha o array
  embaralhado = sorted(lista)

  # Converte o array para string
  for i in range(len(embaralhado)):
    resposta = resposta + embaralhado[i]

  # Converte a palavra para maiúscula e a retorna
  return resposta.upper()

entrada = str(input("Digite uma palavra: "))
print(embaralha(entrada))
