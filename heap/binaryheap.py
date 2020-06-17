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
        lc = None
        if self.size > 1:
            lc = (2 * index) + 1
        return lc if lc < self.size else None

    def rightChild(self, index):
        rc = None
        if self.size > 2:
            rc = (2 * index) + 2
        return rc if rc < self.size else None

    def maxChild(self, index):
        leftC, rightC = self.leftChild(index), self.rightChild(index)
        max_child = None

        if not leftC and not rightC:
            return None

        if leftC == None: 
            max_child = rightC 
        elif rightC == None:
            max_child = leftC
        elif self.heap[leftC] > self.heap[rightC]:
            max_child = leftC
        else:
            max_child = rightC
        
        return max_child

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
            if self.heap[index-1] > self.heap[(index//2)-1]:
                #swap
                temp = self.heap[index-1]
                self.heap[index-1] = self.heap[(index//2)-1]
                self.heap[(index//2)-1] = temp
            index = index // 2
    
    def percolateDown(self, index):
        while (2 * index) < self.size:
            max_child = self.maxChild(index)
            if max_child and self.heap[max_child] > self.heap[index]:
                #swap
                temp = self.heap[index]
                self.heap[index] = self.heap[max_child]
                self.heap[max_child] = temp
            index = max_child


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
            self.heap.pop()
            self.size -= 1
            self.percolateDown(0)
        else:
            self.heap.pop()
            self.size -= 1

        return max_elem
    
    def sort(self):
        pass

    def changePriority(self, position, priority):
        pass

    def print(self):
        print(self.heap)


class MinHeap:
    
    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, index):
        return index/2

    def leftChild(self, index):
        lc = None
        
        if self.size > 1:
            lc = (2 * index) + 1
        return lc if lc < self.size else None

    def rightChild(self, index):
        rc = None

        if self.size > 2:
            rc = (2 * index) + 2
        return rc if rc < self.size else None

    def minChild(self, index):
        leftC, rightC = self.leftChild(index), self.rightChild(index)
        min_child = None

        if not leftC and not rightC:
            return None
        
        if not leftC:
            min_child = rightC
        elif not rightC:
            min_child = leftC
        elif self.heap[leftC] < self.heap[rightC]:
            min_child = leftC
        else:
            min_child = rightC
        
        return min_child

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
            if self.heap[index-1] < self.heap[(index//2)-1]:
                self.heap[index-1], self.heap[(index//2)-1] = self.heap[(index//2)-1], self.heap[index-1]
            index = index // 2

    def percolateDown(self,index):
        while (2 * index) <= self.size:
            min_child = self.minChild(index)
            if min_child and self.heap[min_child] < self.heap[index]:
                #swap 
                temp = self.heap[index]
                self.heap[index] = self.heap[min_child]
                self.heap[min_child] = temp
            index = min_child

    def insert(self, element):
        self.heap.append(element)
        self.size = self.size+1
        self.percolateUp(self.size)

    def getMin(self):
        return self.heap[0]

    def extractMin(self):
        if self.size == 0:
            raise IndexError("no elements in heap.")

        min_elem = self.heap[0]
        if self.size > 1:
            self.heap[0] = self.heap[self.size-1]
            self.heap.pop()
            self.size -= 1
            self.percolateDown(0)
        else:
            self.heap.pop()
            self.size -= 1

        return min_elem

    def Sort(self):
        pass

    def changePriority(self, position, priority):
        pass

    def print(self):
        print(self.heap)


if __name__ == "__main__":
    h = MinHeap()
    h.insert(5)
    h.insert(4)
    h.insert(3)
    h.insert(2)
    h.insert(1)
    h.print()
    print(h.extractMin())
    h.print()

