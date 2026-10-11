import random
import time

inicio = time.perf_counter()

n_testes = 100000
n_maximo = 100
contador = [0] * n_maximo

for i in range(n_testes):
    aleatorio = random.randint(1, n_maximo)
    contador[aleatorio - 1] += 1

lista_ordenada = sorted(contador)

maior_aparicao = lista_ordenada[len(contador) - 1]
n_maior = contador.index(maior_aparicao) + 1

menor_aparicao = lista_ordenada[0]
n_menor = contador.index(menor_aparicao) + 1

media = sum(contador) / n_maximo
media_menor = sum(contador[0:n_maximo // 2 - 1]) / (n_maximo / 2)
media_maior = sum(contador[n_maximo // 2:n_maximo]) / (n_maximo / 2)

for i in range(len(contador)):
    print(f"{i + 1} : {contador[i]}")

print(f"Maior Aparição: {n_maior} : {maior_aparicao} {maior_aparicao / n_testes * 100:.2f}%")
print(f"Menor Aparição: {n_menor} : {menor_aparicao} {menor_aparicao / n_testes * 100:.2f}%")
print(f"Média Aparição: {media} {media / n_testes * 100}%")
print(f"Média Menor: {media_menor}")
print(f"Média Maior: {media_maior}")

fim = time.perf_counter()

duracao = fim - inicio

print(f"Duração: {duracao:.2f} segundos")