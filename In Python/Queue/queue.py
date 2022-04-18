from node import Node


class Queue:
    
    def __init__(self):
        self._size: int = 0
        self.first: Node = None 
        self.last: Node = None 


    def push(self, element) -> None:
        node: Node = Node(element)
        if self.first is None and self.last is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self._size += 1 


    def pop(self):
        if self._size > 0:
            element = self.first.data
            self.first = self.first.next
            self._size -= 1
            
            return element
        raise ValueError("Queue is empty")
            

    def peek(self):
        if self._size > 0:
            element = self.first.data
            return element
        raise ValueError("Queue is empty")
        


    def __repr__(self) -> str:
        if self._size > 0:
            representation: str = ""
            pointer: Node = self.first

            while pointer:
                representation = representation + str(pointer.data) + " "
                pointer = pointer.next
            return representation
        return "Empty queue"
        
        
    def __str__(self) -> str:
        return self.__repr__()
        

    def __len__(self) -> int:
        return self._size