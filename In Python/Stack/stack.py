from node import Node


class Stack:

    def __init__(self):
        self.top: Node = None
        self._size: int = 0   


    def push(self, element) -> None:
        node: Node = Node(element)
        node.next = self.top
        self.top = node
        self._size += 1


    def pop(self):
        if self._size > 0:
            node: Node = self.top
            self.top = self.top.next    
            self._size -= 1
            return node.data
        raise IndexError("The stack is empty")


    def peek(self):
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty")


    def __repr__(self) -> str:
        pointer: Node = self.top
        representation: str = ""
        
        for _ in range(self._size):
            representation = representation + str(pointer.data) + "\n"
            pointer = pointer.next
            
        return representation
        

    def __str__(self) -> str:
        return self.__repr__()
        

    def __len__(self) -> int:
        return self._size