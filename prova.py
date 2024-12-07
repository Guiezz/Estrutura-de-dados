"""
Comando: O dono de um banco precisa criar um software para resolver seus
problemas de gerenciamento de contas e contratou você. Ele pediu para que você
criasse um protótipo de um programa (software) que emule uma aplicação para
gerenciamento de usuários para bancos para verificar se você é a pessoa certa para
o serviço. Nela, deve ser possível cadastrar clientes, excluir clientes, mostrar todos
os clientes do banco e ordená-los pela quantidade de crédito disponível em sua
conta em ordem crescente e decrescente. Cada usuário do banco deve possuir um
nome, um número de conta no banco, um valor da conta (dinheiro que a pessoa
possui naquele exato momento) e o crédito disponível.
OBS: NÃO PODEM SER UTILIZADAS AS FUNÇÕES INSERT, REMOVE, SORT E AFINS
DAS BILIOTECAS DE PYTHON. Realizar o exercício com base no que foi trabalhado
em sala de aula e nos arquivos enviados.
Pontos pela avaliação:
Arquitetura do software (8,00):
• Classe usuário com os devidos atributos (1,00)
• Classe administrar banco com seus devidos atributos (1,00)
• Classe administrar banco com o método de acrescentar usuário (1,00)
• Classe administrar banco com o método de remover usuário (1,00)
• Classe administrar banco com o método de listar usuários (1,00)
• Classe administrar banco com o método de colocar na ordem crescente
usuários de acordo com seu crédito disponível (2,00)
• Classe administrar banco com o método de colocar na ordem
decrescente usuários de acordo com seu crédito disponível (1,00)
Desenvolvimento do software (2,00):
• Crie um software que liste as funções para que uma pessoa possa
interagir e evocar as funções.

"""


class Client:
    def __init__(self, id, name, value_in_account, available_credit):
        self.id = id
        self.name = name
        self.value_in_account = value_in_account
        self.available_credit = available_credit
        self.next = None
        self.previous = None

    def __str__(self):
        return f"\nClient {self.name}, Id {self.id}, has {self.value_in_account} in account and {self.available_credit} available credit."


class Bank:
    def __init__(self):
        self.head = None
        self.tail = None
        self.init_bank()

    def init_bank(self):
        initial_clients = [
            (1, "Guilherme", 100, 1000),
            (2, "Rebeca", 5000, 500),
            (3, "Maria", 3000, 2500),
        ]
        previous_client = None
        for id, name, value_in_account, available_credit in initial_clients:
            new_client = Client(id, name, value_in_account, available_credit)
            if self.head is None:
                self.head = new_client
            else:
                previous_client.next = new_client
                new_client.previous = previous_client
            previous_client = new_client
        self.tail = new_client

    def add_client(self, id, name, value_in_account, available_credit):
        current_client = self.head
        while current_client:
            if current_client.id == id:
                print(f"Erro: Cliente com ID {id} já existe.")
                return
            current_client = current_client.next

        new_client = Client(id, name, value_in_account, available_credit)
        if not self.head:
            self.head = self.tail = new_client
        else:
            self.tail.next = new_client
            new_client.previous = self.tail
            self.tail = new_client
        print(f"\nClient '{name}' added successfully")

    def remove_client(self, id):
        current_client = self.head
        while current_client and current_client.id != id:
            current_client = current_client.next
        if current_client is None:
            print("\nClient not found")
            return
        if current_client.previous:
            current_client.previous.next = current_client.next
        if current_client.next:
            current_client.next.previous = current_client.previous
        if current_client == self.head:
            self.head = current_client.next
        if current_client == self.tail:
            self.tail = current_client.previous
        print(f"\nClient '{current_client.name}' removed successfully")

    def list_clients(self):
        current_client = self.head
        while current_client:
            print(current_client)
            current_client = current_client.next

    def sort_clients_by_credit_ascending(self):
        if not self.head or not self.head.next:
            return

        changed = True
        while changed:
            changed = False
            current = self.head
            while current.next:
                if current.available_credit > current.next.available_credit:
                    next_node = current.next
                    if current.previous:
                        current.previous.next = next_node
                    else:
                        self.head = next_node

                    if next_node.next:
                        next_node.next.previous = current
                    else:
                        self.tail = current

                    current.next = next_node.next
                    next_node.previous = current.previous
                    next_node.next = current
                    current.previous = next_node

                    changed = True
                else:
                    current = current.next

    def sort_clients_by_credit_descending(self):
        if not self.head or not self.head.next:
            return

        changed = True
        while changed:
            changed = False
            current = self.head
            while current.next:
                if current.available_credit < current.next.available_credit:
                    next_node = current.next
                    if current.previous:
                        current.previous.next = next_node
                    else:
                        self.head = next_node

                    if next_node.next:
                        next_node.next.previous = current
                    else:
                        self.tail = current

                    current.next = next_node.next
                    next_node.previous = current.previous
                    next_node.next = current
                    current.previous = next_node

                    changed = True
                else:
                    current = current.next


def main():
    bank = Bank()

    while True:
        print("\nOptions:")
        print("1: List Clients")
        print("2: Add Client")
        print("3: Remove Client")
        print("4: Sort Clients by Credit Ascending")
        print("5: Sort Clients by Credit Descending")
        print("6: Exit")
        option = int(input("Choose an option: "))

        if option == 1:
            bank.list_clients()
        elif option == 2:
            id = int(input("Enter client ID: "))
            name = input("Enter client name: ")
            value_in_account = float(input("Enter account value: "))
            available_credit = float(input("Enter available credit: "))
            bank.add_client(id, name, value_in_account, available_credit)
        elif option == 3:
            id = int(input("Enter client ID to remove: "))
            bank.remove_client(id)
        elif option == 4:
            bank.sort_clients_by_credit_ascending()
            print("\nClients sorted by available credit (ascending).")
        elif option == 5:
            bank.sort_clients_by_credit_descending()
            print("\nClients sorted by available credit (descending).")
            bank.list_clients()
        elif option == 6:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option! Please try again.")


if __name__ == "__main__":
    main()
