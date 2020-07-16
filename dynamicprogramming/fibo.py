

def fibRecursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibRecursive(n-1) + fibRecursive(n-2)


def fibIterative(n):
    prev, curr = 0, 1
    i,next = 0, 0
    while i < n-1:
        next = prev + curr
        prev, curr = curr, next
        i+=1
    return next

def fibDPTopDown(n, memory):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif len(memory) > n:
        return memory[n]
    else:
        num = fibDPTopDown(n-1, memory) + fibDPTopDown(n-2, memory)
        memory.append(num)
        return memory[n]
    

def fibDPBottomUp(n):
    memory = [0] * (n+1)
    memory[1] = 1
    i = 2
    while i <= n:
        memory[i] = memory[i-1] + memory[i-2]
        i+=1
    return memory[n]



if __name__ == "__main__":
    print(fibRecursive(5))
    print(fibIterative(5))
    print(fibDPBottomUp(5))
    print(fibDPTopDown(5,[0,1]))
