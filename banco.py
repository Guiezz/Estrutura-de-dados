#Prova de hoje
class Node:
    def __init__(self, id, balance, name, credit):
        self.id = id
        self.balance = balance
        self.name = name
        self.credit = credit
        self.left = None
        self.right = None
        self.height = 1

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, id, balance, name, credit):
        self.root = self._insert(self.root, id, balance, name, credit)

    def _insert(self, node, id, balance, name, credit):
        if not node:
            return Node(id, balance, name, credit)
        if balance < node.balance:
            node.left = self._insert(node.left, id, balance, name, credit)
        else:
            node.right = self._insert(node.right, id, balance, name, credit)


        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance_factor = self.get_balance_factor(node)

        if balance_factor > 1 and balance < node.left.balance:
            return self.rotate_right(node)
        if balance_factor < -1 and balance > node.right.balance:
            return self.rotate_left(node)
        if balance_factor > 1 and balance > node.left.balance:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance_factor < -1 and balance < node.right.balance:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def remove(self, node, id):
      if not node:
          return node
      if id < node.id:
          node.left = self.remove(node.left, id)
      elif id > node.id:
          node.right = self.remove(node.right, id)
      else:
          if not node.left:
              return node.right
          elif not node.right:
              return node.left

          temp = self.get_min(node.right)
          node.id = temp.id
          node.balance = temp.balance
          node.name = temp.name
          node.credit = temp.credit
          node.right = self.remove(node.right, temp.id)

      node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
      balance_factor = self.get_balance_factor(node)

      if balance_factor > 1 and self.get_balance_factor(node.left) >= 0:
          return self.rotate_right(node)
      if balance_factor > 1 and self.get_balance_factor(node.left) < 0:
          node.left = self.rotate_left(node.left)
          return self.rotate_right(node)
      if balance_factor < -1 and self.get_balance_factor(node.right) <= 0:
          return self.rotate_left(node)
      if balance_factor < -1 and self.get_balance_factor(node.right) > 0:
          node.right = self.rotate_right(node.right)
          return self.rotate_left(node)

      return node


    def search_by_id(self, node, search_id):
        if not node:
            return None
        if node.id == search_id:
            return node
        left_result = self.search_by_id(node.left, search_id)
        if left_result:
            return left_result
        return self.search_by_id(node.right, search_id)


    def get_height(self, node):
        return node.height if node else 0

    def get_balance_factor(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def get_min(self, node):
        return node if not node.left else self.get_min(node.left)

    def rotate_left(self, z):
        y = z.right
        z.right = y.left
        y.left = z
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, z):
        y = z.left
        z.left = y.right
        y.right = z
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

def main():
    tree = Tree()
    while True:
        option = int(input("\n1. Inserir Cliente\n2. Remover Cliente\n3. Buscar Cliente por Id\n4. Sair\nEscolha: "))
        if option == 1:
            id, balance, name, credit = int(input('Insira o Id do cliente: ')), float(input('Insira o valor da conta do cliente: ')), input('Insira o nome do cliente: '), float(input('Insira os cretios do cliente: '))
            tree.insert(id, balance, name, credit)
        elif option == 2:
            balance = float(input("Digite o Id do cliente a ser removeido: "))
            print(f'Removendo Cliente {name}')
            tree.root = tree.remove(tree.root, id)
            print('Cliente removido com sucesso')

        elif option == 3:
            id = int(input("Digite o Id do cliente: "))
            node = tree.search_by_id(tree.root, id)
            print(f"Cliente: {node.name}" if node else "Cliente não encontrado")
        elif option == 4:
            break

if __name__ == "__main__":
    main()
