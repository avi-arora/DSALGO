from SinglyLinkedList import SinglyLinkedList

def hasCycle(list: SinglyLinkedList):
    """
    Detect a cycle using floyd 2 pointer approach
    """
    temp = list
    fastTemp = list
    while temp:
        temp = temp.getNext()
        if fastTemp.getNext().getNext():
            fastTemp = fastTemp.getNext().getNext()
        if temp == fastTemp:
            return 1
    return 0


if __name__ == "__main__":
    l = SinglyLinkedList()

    l.insertAtFront(5)
    l.insertAtFront(4)
    l.insertAtFront(3)
    l.insertAtFront(2)
    l.insertAtFront(1)

    l.print()

    #modify list to create a cycle
    l.getNext().getNext().setNext(l.getNext())

  #  l.print()

    print(hasCycle(l))
    