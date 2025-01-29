class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaDeBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        """Insere um saldo na Ã¡rvore."""
        if self.raiz is None:
            self.raiz = Node(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.esquerda is None:
                nodo.esquerda = Node(valor)
            else:
                self._inserir_recursivo(nodo.esquerda, valor)
        else:
            if nodo.direita is None:
                nodo.direita = Node(valor)
            else:
                self._inserir_recursivo(nodo.direita, valor)

    def remover(self, valor):
        """Remove um saldo da Ã¡rvore."""
        self.raiz = self._remover_recursivo(self.raiz, valor)

    def _remover_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.esquerda = self._remover_recursivo(nodo.esquerda, valor)
        elif valor > nodo.valor:
            nodo.direita = self._remover_recursivo(nodo.direita, valor)
        else:
            if nodo.esquerda is None:
                return nodo.direita
            elif nodo.direita is None:
                return nodo.esquerda
            
            temp = self._valor_minimo(nodo.direita)
            nodo.valor = temp.valor
            nodo.direita = self._remover_recursivo(nodo.direita, temp.valor)
        
        return nodo

    def _valor_minimo(self, nodo):
        atual = nodo
        while(atual.esquerda is not None):
            atual = atual.esquerda
        return atual

    def pre_ordem(self):
        """Percorre a Ã¡rvore em prÃ©-ordem."""
        self._pre_ordem_recursivo(self.raiz)
        print()

    def _pre_ordem_recursivo(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self._pre_ordem_recursivo(nodo.esquerda)
            self._pre_ordem_recursivo(nodo.direita)

    def em_ordem(self):
        """Percorre a Ã¡rvore em-ordem."""
        self._em_ordem_recursivo(self.raiz)
        print()

    def _em_ordem_recursivo(self, nodo):
        if nodo:
            self._em_ordem_recursivo(nodo.esquerda)
            print(nodo.valor, end=" ")
            self._em_ordem_recursivo(nodo.direita)

    def pos_ordem(self):
        """Percorre a Ã¡rvore em pÃ³s-ordem."""
        self._pos_ordem_recursivo(self.raiz)
        print()

    def _pos_ordem_recursivo(self, nodo):
        if nodo:
            self._pos_ordem_recursivo(nodo.esquerda)
            self._pos_ordem_recursivo(nodo.direita)
            print(nodo.valor, end=" ")

# Exemplo de uso:
bst = ArvoreBinariaDeBusca()
bst.inserir(50)
bst.inserir(30)
bst.inserir(70)
bst.inserir(20)
bst.inserir(40)
bst.inserir(60)
bst.inserir(80)

print("Percurso em prÃ©-ordem:")
bst.pre_ordem()

print("Percurso em-ordem:")
bst.em_ordem()

print("Percurso em pÃ³s-ordem:")
bst.pos_ordem()

print("Removendo o valor 50:")
bst.remover(50)
print("Percurso em-ordem apÃ³s remoÃ§Ã£o:")
bst.em_ordem()