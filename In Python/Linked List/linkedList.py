from node import Node

class LinkedList:

    def __init__(self):
        self.head: Node = None
        self._size: int = 0   

    
    def append(self, element) -> None:
        if self.head:
            pointer: Node = self.head
            
            while pointer.next:
                pointer = pointer.next
            
            pointer.next = Node(element)
        else:
            self.head = Node(element)
        
        self._size += 1


    def __len__(self) -> int:
        return self._size


    def _get_node(self, index: int) -> Node:
        pointer: Node = self.head

        for _ in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        
        return pointer


    def get_index(self, element) -> int: 
        pointer: Node = self.head
        index: int = 0

        while(pointer):
            if pointer.data == element:
                return index
            pointer = pointer.next

            index += 1
    
        raise ValueError(f"{element} is not in list")


    def __getitem__(self, index: int):
        pointer: Node = self._get_node(index)
        
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range")


    def __setitem__(self, index: int, element) -> None:
        pointer: Node = self._get_node(index)

        if pointer:
            pointer.data = element
        else:
            raise IndexError("list index out of range")


    def insert(self, index: int, element) -> None:
        node: Node = Node(element)

        if index == 0:
            node.next = self.head
            self.head = node 
        else:
            pointer: Node = self._get_node(index - 1)
            node.next = pointer.next                 
            pointer.next = node
    
        self._size += 1


    def remove(self, element):
        previous: Node = None 
        pointer: Node = self.head
        
        while pointer:
            if pointer.data == element:
                break
            else:
                previous = pointer
                pointer = pointer.next

        if not pointer:
            raise ValueError(f"{element} is not in list")
        else:
            """if there is a previous, then we aren't at the head"""
            if previous:
                previous.next = pointer.next
                pointer.next = None
                self._size -= 1
            else:
                self.head = pointer.next
                pointer.next = None
                self._size -= 1


    def __repr__(self) -> str:
        pointer: Node = self.head
        representation: str = ""
        
        for i in range(self._size):
            if i != self._size - 1:
                representation = representation + str(pointer.data) + " -> "
                pointer = pointer.next
            else:
                representation = representation + str(pointer.data)
        return representation
        

    def __str__(self) -> str:
        return self.__repr__()
        