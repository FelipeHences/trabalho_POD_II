class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = No(chave)
        else:
            self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, no, chave):
        if chave < no.chave:
            if no.esquerda is None:
                no.esquerda = No(chave)
            else:
                self._inserir_recursivo(no.esquerda, chave)
        else:
            if no.direita is None:
                no.direita = No(chave)
            else:
                self._inserir_recursivo(no.direita, chave)

    def pesquisar(self, chave):
        return self._pesquisar_recursivo(self.raiz, chave)

    def _pesquisar_recursivo(self, no, chave):
        if no is None or no.chave == chave:
            return no
        if chave < no.chave:
            return self._pesquisar_recursivo(no.esquerda, chave)
        else:
            return self._pesquisar_recursivo(no.direita, chave)
