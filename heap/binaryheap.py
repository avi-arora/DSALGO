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

    def maxChild(self, index):
        """
        returns index of maximum child of a node at index
        to access child 

        """
        leftC, rightC = self.leftChild(index), self.rightChild(index)
        if self.heap[leftC] > self.heap[rightC]:
            return leftC
        else:
            return rightC

    def isLeaf(self, index):
        return self.leftChild(index) > self.size \
            and self.rightChild(index) > self.size  

    def correctionUP(self):
        index = self.size // 2
        while index >= 0:
            if not self.isLeaf(index):
                maxCIndex = self.maxChild(index)
                if self.heap[maxCIndex] > self.heap[index]:
                    #swap
                    temp = self.heap[index]
                    self.heap[index] = self.heap[maxCIndex]
                    self.heap[maxCIndex] = temp

            index -= 1

    def correctionDown(self):
        pass

    def percolateUp(self, index):
        while index // 2 > 0:
            #if node is greater than it's parent
            if self.heap[index] > self.heap[index//2]:
                #swap
                temp = self.heap[index]
                self.heap[index] = self.heap[index//2]
                self.heap[index//2] = temp
            index = index // 2
    
    def percolateDown(self, index):
        while index < self.size // 2:
            max_child = self.maxChild(0)
            if self.heap[max_child] > self.heap[index]:
                #swap
                temp = self.heap[index]
                self.heap[index] = self.heap[max_child]
                self.heap[max_child] = temp
            index -= 1


    def insert(self, element):
        self.heap.append(element)
        self.size = self.size+1
        self.percolateUp(self.size-1)

    def getMax(self):
        return self.heap[0]

    def extractMax(self):
        if self.size == 0:
            raise IndexError("no elements in heap.")

        max_elem = self.heap[0]
        if self.size > 1:
            self.heap[0] = self.heap[self.size-1]
            self.percolateDown(0)
        else:
            self.heap.pop()

        return max_elem
    
    def sort(self):
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

    def minChild(self, index):
        leftC, rightC = self.leftChild(index), self.rightChild(index)
        if self.heap[leftC] < self.heap[rightC]:
            return leftC
        else:
            return rightC

    def isLeaf(self, index):
        return self.leftChild(index) > self.size \
            and self.rightChild(index) > self.size

    def correctionUp(self):
        index = self.size // 2
        while index >= 0:
            if not self.isLeaf(index):
                minCIndex = self.minChild(index)
                if self.heap[minCIndex] < self.heap[index]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[minCIndex]
                    self.heap[minCIndex] = temp
            index -= 1

    def percolateUp(self, index):
        while index // 2 > 0:
            if self.heap[index] < self.heap[index//2]:
                self.heap[index], self.heap[index//2] = self.heap[index//2], self.heap[index]
            index = index // 2

    def percolateDown(self,index):
        while index < self.size // 2:
            min_child = self.minChild(index)
            if self.heap[min_child] < self.heap[index]:
                #swap 
                temp = self.heap[index]
                self.heap[index] = self.heap[min_child]
                self.heap[min_child] = temp
            index -= 1

    def insert(self, element):
        self.heap.append(element)
        self.size = self.size+1
        self.percolateUp(self.size-1)

    def getMin(self):
        return self.heap[0]

    def extractMin(self):
        if self.size == 0:
            raise IndexError("no elements in heap.")

        min_elem = self.heap[0]
        if self.size > 1:
            self.heap[0] = self.heap[self.size-1]
            self.percolateDown(0)
        else:
            self.heap.pop()

        return min_elem

    def Sort(self):
        pass

