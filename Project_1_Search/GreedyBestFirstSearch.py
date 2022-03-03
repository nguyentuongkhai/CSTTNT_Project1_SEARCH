from general import*
from math import*

def heuristic(currentNode, endNode):
    return sqrt((currentNode[0] - endNode[0])**2 + (currentNode[1] - endNode[1])**2)

def GBFSearch(graph, startNode, endNode):
    visited = [startNode]   # lưu các node đã đi qua
    previous = {}   # previous[n] gồm các node đi qua trước node n
    queue = [startNode]
    H = {}  # H(n) là giá trị heuristic tại n
    H[startNode] = heuristic(startNode, endNode)
    while queue:
        f = {}
        for i in queue:
            f[i] = H[i]
        currentNode = getKeyOfMinValue(f)
        del f

        if currentNode == endNode:
            return findRoute(startNode, endNode, previous)

        queue.remove(currentNode)
        for neighbor in graph[currentNode]:
            if neighbor not in visited:
                H[neighbor] = heuristic(neighbor, endNode)
                visited.append(neighbor)
                previous[neighbor] = currentNode
                queue.append(neighbor)
    return False