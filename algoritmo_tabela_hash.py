class TabelaHash:
    def __init__(self):
        self.tamanho = 10  # Tamanho da tabela de hash
        self.tabela = [[] for _ in range(self.tamanho)]  # Inicializa a tabela de hash vazia

    def funcao_hash(self, chave):
        # Função de hash simples para este exemplo (pode ser adaptada conforme necessário)
        return chave % self.tamanho

    def inserir(self, chave, valor):
        indice = self.funcao_hash(chave)
        lista = self.tabela[indice]

        for item in lista:
            if item[0] == chave:  # Verifica se a chave já existe na tabela
                item[1] = valor  # Atualiza o valor se a chave já existe
                return

        lista.append([chave, valor])  # Insere a chave e o valor na lista

    def pesquisar(self, chave):
        indice = self.funcao_hash(chave)
        lista = self.tabela[indice]

        for item in lista:
            if item[0] == chave:
                return item[1]  # Retorna o valor associado à chave

        return None  # Retorna None se a chave não for encontrada


# Exemplo de uso
tabela_hash = TabelaHash()

# Inserção de elementos
tabela_hash.inserir(5, "Valor 1")
tabela_hash.inserir(12, "Valor 2")
tabela_hash.inserir(20, "Valor 3")

# Pesquisa de elementos
resultado1 = tabela_hash.pesquisar(5)
print(resultado1)  # Saída: Valor 1

resultado2 = tabela_hash.pesquisar(12)
print(resultado2)  # Saída: Valor 2

resultado3 = tabela_hash.pesquisar(20)
print(resultado3)  # Saída: Valor 3

resultado4 = tabela_hash.pesquisar(8)
print(resultado4)  # Saída: None (chave não encontrada)
