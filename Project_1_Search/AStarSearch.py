from general import*
from math import*

def heuristic_no_bonus(node, endNode):
    # Trả về Euclidean distance
    return sqrt((node[0]-endNode[0])**2 + (node[1]-endNode[1])**2)


def heuristic_bonus(node):
    # Trả về -(điểm thưởng) nếu node đó có điểm thưởng
    # Hoặc trả về 0 nếu node không có điểm thưởng
    if(type(node) is tuple):
        if(len(node)==3):
            return node[2] #+ heuristic_no_bonus(node, (1,0))
    return 0 #+ heuristic_no_bonus(node, (1,0))

def AStarSearch(graph, startNode, endNode, Bonus=False):
    listOpenNodes = [startNode]
    listCloseNodes = []
    previous = {} # luu node cha node con
    route = [endNode]

    # Trường hợp bản đò không có điểm thưởng
    if Bonus == False:
        G = {}  # lưu giá trị thực tính từ start node dến các node khác
        G[startNode] = 0    # = giá trị khoảng cách thực từ startNode -> startNode

        F = {}  # lưu giá trị hàm f(n)
        F[startNode] = G[startNode] + heuristic_no_bonus(startNode,endNode)
        while listOpenNodes:
            # Lấy node tốt nhất trong Open
            # get value of node in list of opened node
            f = {}
            for i in listOpenNodes:
                f[i] = F[i]
            currentNode = getKeyOfMinValue(f)
            del f
            if(currentNode == endNode):
                while route[-1] != startNode:
                    route.append(previous[route[-1]])
                route.reverse()
                return route
            
            listOpenNodes.remove(currentNode)
            listCloseNodes.append(currentNode)
            for neighbor in graph[currentNode]:
                if(neighbor in listOpenNodes):
                    if(G[neighbor] > G[currentNode] + 1):
                        G[neighbor] = G[currentNode] + 1
                        F[neighbor] = G[neighbor] + heuristic_no_bonus(neighbor, endNode)
                        previous[neighbor] = currentNode

                elif(neighbor in listCloseNodes):
                    if (G[neighbor] > G[currentNode] + 1):
                        listCloseNodes.remove(neighbor)
                        listOpenNodes.append(neighbor)
                
                elif (neighbor not in listOpenNodes):
                # else:
                    G[neighbor] = G[currentNode] + 1
                    F[neighbor] = G[neighbor] + heuristic_no_bonus(neighbor, endNode)
                    previous[neighbor] = currentNode
                    listOpenNodes.append(neighbor)

    # Trường hợp bản đồ có điểm thưởng
    else:
        G = {}  # lưu giá trị thực tính từ start node dến các node khác
        G[startNode] = 0    # = giá trị khoảng cách thực từ startNode -> startNode

        F = {}  # lưu giá trị hàm f(n)
        F[startNode] = G[startNode] + heuristic_bonus(startNode) 
        while listOpenNodes:
            # Lấy node tốt nhất trong Open
            # get value of node in list of opened node
            f = {}
            for i in listOpenNodes:
                f[i] = F[i]
            currentNode = getKeyOfMinValue(f)
            del f
            if(currentNode == endNode):
                while route[-1] != startNode:
                    route.append(previous[route[-1]])
                route.reverse()
                return route
            
            listOpenNodes.remove(currentNode)
            listCloseNodes.append(currentNode)
            for neighbor in graph[currentNode]:
                if(neighbor in listOpenNodes):
                    if(G[neighbor] > G[currentNode] + 1):
                        G[neighbor] = G[currentNode] + 1
                        F[neighbor] = G[neighbor] + heuristic_bonus(neighbor)
                        #G[neighbor] = G[neighbor] + heuristic_bonus(neighbor)
                        previous[neighbor] = currentNode

                elif(neighbor in listCloseNodes):
                    if (G[neighbor] > G[currentNode] + 1):
                        listCloseNodes.remove(neighbor)
                        listOpenNodes.append(neighbor)
                
                elif (neighbor not in listOpenNodes):
                # else:
                    G[neighbor] = G[currentNode] + 1
                    F[neighbor] = G[neighbor] + heuristic_bonus(neighbor)
                    #G[neighbor] = G[neighbor] + heuristic_bonus(neighbor)
                    previous[neighbor] = currentNode
                    listOpenNodes.append(neighbor)
    
    return False
