class MaxHeap:

    def __init__(self):
        self.heap = []
        self.size = 0
        

    def parent(self, index):
        """
        Parent of a node always store at i/2 location in binary heap
        """
        return index / 2

    def leftChild(self, index):
        """
        """
        return (2 * index) + 1

    def rightChild(self, index):
        """
        """
        return (2 * index) + 2

    def percolateUp(self):
        pass

    def percolateDown(self):
        pass


class MinHeap:
    
    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, index):
        return index/2

    def leftChild(self, index):
        return (2 * index) + 1

    def rightChild(self, index):
        """
        if array are not 0 indexed based then 2i+1 is exact position of index
        """
        return (2 * index) + 2

    def percolateUp(self):
        pass

    def percolateDown(self):
        pass
