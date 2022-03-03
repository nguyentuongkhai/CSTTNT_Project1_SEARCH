from general import*

def BFSearch (graph, startNode, endNode):
    visited = [startNode]
    previous = {}
    queue = [startNode]
    while queue:
        currentNode = queue.pop(0)
        if currentNode == endNode:
            return findRoute(startNode, endNode, previous)
        
        for neighbor in graph[currentNode]:
            if neighbor not in visited:
                visited.append(neighbor)
                previous[neighbor] = currentNode
                queue.append(neighbor)
    
    return False

