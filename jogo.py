# Exercicio de Redes de Computadores

from random import sample

print("-=-=-=-" * 10)
print("Bem vindo, tente acerta os números da mega da virada")
print("-=-=-=-" * 10)

# 1. Contador do computador
computador = 5
# 2. Coletar números do usuário e colocar em lista
numeros_usuario = []
contador = 0

while contador < computador:
    escolha_numero = int(input(f"Digite o número {contador + 1}: "))
    contador += 1
    numeros_usuario.append(escolha_numero) # append vai adicionar os números escolhido pelo usuario e alocar em uma lista 
# 3. Gerar números aleatórios
numeros_aleatorios = sample(range(1, 50), computador) # números entr 1 e 50

# 4.Verificar os acertos dos números do usuários
acertos = []
while escolha_numero == numeros_usuario:
    if escolha_numero == numeros_aleatorios:
        acertos.append() # Vai verificar se os números digitado pelo usuario estão corretos
# 4. Mostrar os resutados
print(f"Número digitado pelo usuário: {numeros_usuario}")

print(f"Números sorteados pelo computador: {numeros_aleatorios}")

print(f"Números acertadors: {acertos}")