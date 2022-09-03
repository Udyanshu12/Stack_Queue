from node import Node


class Stack(Node):
    def __init__(self, value):
        super().__init__(value)
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        if self.height == 1:
            self.top = None
        else:
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp
