from Node import Node

class AVLTree:
    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0

    def get_height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def insert(self, key, movie):
        tree = self.node
        new_node = Node(key, movie)

        if tree is None:
            self.node = new_node
            self.node.left = AVLTree()
            self.node.right = AVLTree()

        elif key < tree.key:
            self.node.left.insert(key, movie)

        elif key > tree.key:
            self.node.right.insert(key, movie)

        self.re_balance_tree()

    def re_balance_tree(self):
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.rotate_left()
                    self.update_heights()
                    self.update_balances()
                self.rotate_right()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rotate_right()
                    self.update_heights()
                    self.update_balances()
                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def rotate_right(self):
        root = self.node
        left_child = self.node.left.node
        right_child = left_child.right.node

        self.node = left_child
        left_child.right.node = root
        root.left.node = right_child

    def rotate_left(self):
        root = self.node
        right_child = self.node.right.node
        left_child = right_child.left.node

        self.node = right_child
        right_child.left.node = root
        root.right.node = left_child

    def update_heights(self, recurse=True):
        if not self.node is None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_heights()
                if self.node.right is not None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.node is None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_balances()
                if self.node.right is not None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def check_balanced(self):
        if self is None or self.node is None:
            return True

        self.update_heights()
        self.update_balances()
        return ((abs(
            self.balance) < 2) and self.node.left.check_balanced() and
                self.node.right.check_balanced())

    def tree_in_order(self):
        if self.node is None:
            return []
        nodes_list = []
        l = self.node.left.tree_in_order()
        for i in l:
            nodes_list.append(i)

        nodes_list.append(self.node.movie.id)

        l = self.node.right.tree_in_order()
        for i in l:
            nodes_list.append(i)
        lista = nodes_list
        lista.sort()
        return lista

    def print_tree(self, node=None, level=0):
        if not node:
            node = self.node

        if node.right.node:
            self.print_tree(node.right.node, level + 1)
            print(('\t' * level), (' / '))
        print(('\t' * level), node.key)

        if node.left.node:
            print(('\t' * level), (' \\ '))
            self.print_tree(node.left.node, level + 1)
    
    def find_by_id(self, id):
        tree = self.node
        if tree == None:
            print('ID não encontrado')

        else:    
            if id == tree.key:
                print('ID:',tree.movie.id)
                print('Nome:',tree.movie.nome)
                print('Ano:',tree.movie.ano)
                print()
            
            elif id > tree.key:
                tree.right.find_by_id(id)
            
            elif id < tree.key:
                tree.left.find_by_id(id)

    def find_by_year(self, year):
        lista = []
        if self.node is None:
            return []

        if self.node.movie.ano == year:
            print(self.node.movie)
        
        else:
            self.node.left.tree_in_order()
            self.node.right.tree_in_order()

        print(lista)
        return lista        

    def __str__(self):
        return '{}'.format(self.node.movie)