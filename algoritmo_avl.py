class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1


class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        self.raiz = self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, no, chave):
        if no is None:
            return No(chave)
        elif chave < no.chave:
            no.esquerda = self._inserir_recursivo(no.esquerda, chave)
        else:
            no.direita = self._inserir_recursivo(no.direita, chave)

        no.altura = 1 + max(self._obter_altura(no.esquerda), self._obter_altura(no.direita))

        fator_balanceamento = self._calcular_fator_balanceamento(no)

        if fator_balanceamento > 1:
            if chave < no.esquerda.chave:
                return self._rotacao_direita(no)
            else:
                no.esquerda = self._rotacao_esquerda(no.esquerda)
                return self._rotacao_direita(no)

        if fator_balanceamento < -1:
            if chave > no.direita.chave:
                return self._rotacao_esquerda(no)
            else:
                no.direita = self._rotacao_direita(no.direita)
                return self._rotacao_esquerda(no)

        return no

    def _rotacao_direita(self, z):
        y = z.esquerda
        T3 = y.direita

        y.direita = z
        z.esquerda = T3

        z.altura = 1 + max(self._obter_altura(z.esquerda), self._obter_altura(z.direita))
        y.altura = 1 + max(self._obter_altura(y.esquerda), self._obter_altura(y.direita))

        return y

    def _rotacao_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda

        y.esquerda = z
        z.direita = T2

        z.altura = 1 + max(self._obter_altura(z.esquerda), self._obter_altura(z.direita))
        y.altura = 1 + max(self._obter_altura(y.esquerda), self._obter_altura(y.direita))

        return y

    def _obter_altura(self, no):
        if no is None:
            return 0
        return no.altura

    def _calcular_fator_balanceamento(self, no):
        if no is None:
            return 0
        return self._obter_altura(no.esquerda) - self._obter_altura(no.direita)

    def pesquisar(self, chave):
        return self._pesquisar_recursivo(self.raiz, chave)

    def _pesquisar_recursivo(self, no, chave):
        if no is None or no.chave == chave:
            return no
        if chave < no.chave:
            return self._pesquisar_recursivo(no.esquerda, chave)
        else:
            return self._pesquisar_recursivo(no.direita, chave)
