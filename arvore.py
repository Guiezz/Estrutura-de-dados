class NoAVL:
    def __init__(self, numero_conta, saldo, nome, credito):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.nome = nome
        self.credito = credito
        self.altura = 1
        self.esquerda = None
        self.direita = None

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def inserir(self, no, numero_conta, saldo, nome, credito):
        if not no:
            return NoAVL(numero_conta, saldo, nome, credito)

        if credito < no.credito:  # Comparar pelo crÃ©dito
            no.esquerda = self.inserir(no.esquerda, numero_conta, saldo, nome, credito)
        else:
            no.direita = self.inserir(no.direita, numero_conta, saldo, nome, credito)

        no.altura = 1 + max(self.obter_altura(no.esquerda), self.obter_altura(no.direita))

        fator_balanceamento = self.obter_balanceamento(no)

        if fator_balanceamento > 1 and credito < no.esquerda.credito:  # Comparar pelo crÃ©dito
            return self.rotacionar_direita(no)
        if fator_balanceamento < -1 and credito > no.direita.credito:  # Comparar pelo crÃ©dito
            return self.rotacionar_esquerda(no)
        if fator_balanceamento > 1 and credito > no.esquerda.credito:  # Comparar pelo crÃ©dito
            no.esquerda = self.rotacionar_esquerda(no.esquerda)
            return self.rotacionar_direita(no)
        if fator_balanceamento < -1 and credito < no.direita.credito:  # Comparar pelo crÃ©dito
            no.direita = self.rotacionar_direita(no.direita)
            return self.rotacionar_esquerda(no)

        return no

    def remover(self, no, credito):
        if not no:
            return no

        if credito < no.credito:  # Comparar pelo crÃ©dito
            no.esquerda = self.remover(no.esquerda, credito)
        elif credito > no.credito:  # Comparar pelo crÃ©dito
            no.direita = self.remover(no.direita, credito)
        else:
            if not no.esquerda:
                return no.direita
            elif not no.direita:
                return no.esquerda

            temp = self.obter_no_minimo(no.direita)
            no.credito = temp.credito
            no.numero_conta = temp.numero_conta
            no.saldo = temp.saldo
            no.nome = temp.nome
            no.direita = self.remover(no.direita, temp.credito)

        no.altura = 1 + max(self.obter_altura(no.esquerda), self.obter_altura(no.direita))

        fator_balanceamento = self.obter_balanceamento(no)

        if fator_balanceamento > 1 and self.obter_balanceamento(no.esquerda) >= 0:
            return self.rotacionar_direita(no)
        if fator_balanceamento < -1 and self.obter_balanceamento(no.direita) <= 0:
            return self.rotacionar_esquerda(no)
        if fator_balanceamento > 1 and self.obter_balanceamento(no.esquerda) < 0:
            no.esquerda = self.rotacionar_esquerda(no.esquerda)
            return self.rotacionar_direita(no)
        if fator_balanceamento < -1 and self.obter_balanceamento(no.direita) > 0:
            no.direita = self.rotacionar_direita(no.direita)
            return self.rotacionar_esquerda(no)

        return no

    def buscar(self, no, credito):
        if not no or no.credito == credito:  # Comparar pelo crÃ©dito
            return no
        if credito < no.credito:  # Comparar pelo crÃ©dito
            return self.buscar(no.esquerda, credito)
        return self.buscar(no.direita, credito)

    def rotacionar_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda
        y.esquerda = z
        z.direita = T2
        z.altura = 1 + max(self.obter_altura(z.esquerda), self.obter_altura(z.direita))
        y.altura = 1 + max(self.obter_altura(y.esquerda), self.obter_altura(y.direita))
        return y

    def rotacionar_direita(self, z):
        y = z.esquerda
        T3 = y.direita
        y.direita = z
        z.esquerda = T3
        z.altura = 1 + max(self.obter_altura(z.esquerda), self.obter_altura(z.direita))
        y.altura = 1 + max(self.obter_altura(y.esquerda), self.obter_altura(y.direita))
        return y

    def obter_altura(self, no):
        if not no:
            return 0
        return no.altura

    def obter_balanceamento(self, no):
        if not no:
            return 0
        return self.obter_altura(no.esquerda) - self.obter_altura(no.direita)

    def obter_no_minimo(self, no):
        if no is None or no.esquerda is None:
            return no
        return self.obter_no_minimo(no.esquerda)

def exibir_menu():
    print("\nMenu:")
    print("1. Inserir Novo Cliente")
    print("2. Remover Cliente")
    print("3. Buscar Cliente pelo CrÃ©dito")
    print("4. Sair")

def main():
    arvore = ArvoreAVL()

    # Clientes iniciais
    clientes_iniciais = [
        (1, 1000.0, "Daniel", 5000.0),
        (2, 2000.0, "Pedro", 4000.0),
        (3, 1500.0, "Gabriel", 3000.0),
        (4, 1800.0, "Henrique", 3500.0),
        (5, 1700.0, "Evelyn", 3200.0),
        (6, 1900.0, "Franklin", 2800.0),
        (7, 1600.0, "Graciane", 3700.0),
        (8, 1750.0, "JoÃ£o", 3300.0),
    ]

    for numero_conta, saldo, nome, credito in clientes_iniciais:
        arvore.raiz = arvore.inserir(arvore.raiz, numero_conta, saldo, nome, credito)

    while True:
        exibir_menu()
        try:
            opcao = int(input("Escolha uma opÃ§Ã£o: "))

            if opcao == 1:
                numero_conta = int(input("NÃºmero da Conta Corrente: "))
                saldo = float(input("Saldo na Conta: "))
                nome = input("Nome: ")
                credito = float(input("Valor de CrÃ©dito: "))
                arvore.raiz = arvore.inserir(arvore.raiz, numero_conta, saldo, nome, credito)
                print(f"Cliente {nome} inserido com sucesso.")

            elif opcao == 2:
                credito = float(input("CrÃ©dito do Cliente a ser removido: "))  # Remover pelo crÃ©dito
                arvore.raiz = arvore.remover(arvore.raiz, credito)
                print(f"Cliente com crÃ©dito {credito} removido com sucesso.")

            elif opcao == 3:
                credito = float(input("CrÃ©dito do Cliente a ser buscado: "))  # Buscar pelo crÃ©dito
                resultado = arvore.buscar(arvore.raiz, credito)
                if resultado:
                    print(f"Cliente encontrado: Nome: {resultado.nome}, Conta: {resultado.numero_conta}, Saldo: {resultado.saldo}, CrÃ©dito: {resultado.credito}")
                else:
                    print("Cliente nÃ£o encontrado.")

            elif opcao == 4:
                print("Saindo do sistema...")
                break

            else:
                print("OpÃ§Ã£o invÃ¡lida. Tente novamente.")

        except ValueError:
            print("Entrada invÃ¡lida. Por favor, insira um nÃºmero.")

if __name__ == "__main__":
    main()