import math

def jump_search(lista, chave):
    tamanho = len(lista)
    tamanho_salto = int(math.sqrt(tamanho))

    # Encontrando o bloco onde a chave pode estar presente
    bloco_atual = 0
    while bloco_atual < tamanho and lista[bloco_atual] < chave:
        bloco_atual += tamanho_salto

    # Realizando pesquisa linear dentro do bloco
    inicio_bloco = bloco_atual - tamanho_salto
    for i in range(inicio_bloco, min(bloco_atual, tamanho)):
        if lista[i] == chave:
            return i  # Elemento encontrado

    return -1  # Elemento não encontrado

# Exemplo de uso
lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
chave = 12

resultado = jump_search(lista, chave)
if resultado != -1:
    print(f"A chave {chave} foi encontrada no índice {resultado}.")
else:
    print(f"A chave {chave} não foi encontrada na lista.")
