from general import*

def DFSearch (graph, startNode,endNode):
    previous = dict()
    visited = list()
    stack = [startNode]
    while stack:
        currentNode = stack.pop()
        if(currentNode == endNode):
            return findRoute(startNode, endNode, previous)
        
        for neighbor in graph[currentNode]:
            if neighbor not in visited:
                visited.append(neighbor)
                previous[neighbor] = currentNode
                stack.append(neighbor)
    return False


