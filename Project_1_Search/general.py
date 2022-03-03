import os
import sys
import matplotlib.pyplot as plt
from collections import defaultdict

# Tìm key chứa value nhỏ nhất trong dict()
def getKeyOfMinValue (d):
    if(type(d) is dict):
        minValue = min(d.values())
        for key in d:
            if d[key] == minValue:
                return key
    return False

# Tìm đường (route) dựa trên node đầu, nốt cuối và danh dách các node nối nhau
def findRoute(startNode, endNode, previous):
    S = 0
    route = [endNode]
    while route[-1] != startNode:
        route.append(previous[route[-1]])
    route.reverse()
    return route

# TÌm chiều dài đuòng đi
def lengthOfRoute(route, bonus=False):
    # Trong trường hợp không phải bản đồ điểm thưởng thì trả về chiều dài thực của route
    # Trường hợp là bản đồ có điểm thưởng thì trả về chiều dài route sau khi trừ đi các điểm thưởng
    S = len(route)
    if bonus == True:
        for i in range(len(route)):
            if len(route[i]) == 3:
                S = S - route[i][2]
    return S

# Hàm đọc bản đồ từ .txt
def read_file(file_name: str = 'maze.txt'):
    f=open(file_name,'r')
    # Đọc danh sách các điểm thưởng có trong bản đồ
    n_bonus_points = int(next(f)[:-1])
    bonus_points = []
    for i in range(n_bonus_points):
        x, y, reward = map(int, next(f)[:-1].split(' '))
        bonus_points.append((x, y, reward))

    text=f.read()
    matrix=[list(i) for i in text.splitlines()]
    rowNumber = len(matrix)
    colNumber = len(matrix[0])
    graph = defaultdict(list)
    for i in range(rowNumber):
        for j in range(colNumber):
            if matrix[i][j]=='S':
                start=(i, j)

            if matrix[i][j] != 'x':
                if (matrix[i][j] == ' ') and ((i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1)):
                    end=(i, j)
                # Lấy phần tử kề trên của node (i,j)
                current = (i,j)
                for point in bonus_points:
                    if (point[0] == i) and (point[1] == j):
                        current = point
                if( i - 1 >= 0 ) and matrix[i-1][j] != 'x':
                    flag = True
                    for point in bonus_points:
                        if(point[0] == i-1 and point[1] == j):
                            graph[current].append(point)
                            flag = False
                    if flag == True:
                        graph[current].append((i-1,j))
                # Lấy phần tử kề dưới của i,j
                if( i + 1 <= rowNumber - 1 ) and matrix[i+1][j]!='x':
                    flag = True
                    for point in bonus_points:
                        if(point[0] == i+1 and point[1] == j):
                            graph[current].append(point)
                            flag = False
                    if flag == True:
                        graph[current].append((i+1,j))
                # Lấy phần tử kề trái của (i,j)
                if( j - 1 >= 0  ) and matrix[i][j-1]!='x':
                    flag = True
                    for point in bonus_points:
                        if(point[0] == i and point[1] == j-1):
                            graph[current].append(point)
                            flag = False
                    if flag == True:
                        graph[current].append((i,j-1))
                # Lấy phần tử kề phải của (i,j)
                if( j + 1 <= colNumber - 1 ) and matrix[i][j+1] != 'x':
                    flag = True
                    for point in bonus_points:
                        if(point[0] == i and point[1] == j+1):
                            graph[current].append(point)
                            flag = False
                    if flag == True:
                        graph[current].append((i,j+1))
    
    f.close()
    return matrix, bonus_points, graph, start, end

# Hàm vẽ bản đồ và đường đi lên figure
def visualize_maze(matrix, bonus, start, end, route=None):
    """
    Args:
      1. matrix: The matrix read from the input file,
      2. bonus: The array of bonus points,
      3. start, end: The starting and ending points,
      4. route: The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
    """
    #1. Define walls and array of direction based on the route
    walls=[(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j]=='x']

    if route:
        direction=[]
        for i in range(1,len(route)):
            if route[i][0]-route[i-1][0]>0:
                direction.append('v') #^
            elif route[i][0]-route[i-1][0]<0:
                direction.append('^') #v        
            elif route[i][1]-route[i-1][1]>0:
                direction.append('>')
            else:
                direction.append('<')

        direction.pop(0)

    #2. Drawing the map
    ax=plt.figure(dpi=100).add_subplot(111)

    for i in ['top','bottom','right','left']:
        ax.spines[i].set_visible(False)

    plt.scatter([i[1] for i in walls],[-i[0] for i in walls],
                marker='X',s=100,color='black')
    
    plt.scatter([i[1] for i in bonus],[-i[0] for i in bonus],
                marker='P',s=100,color='green')

    plt.scatter(start[1],-start[0],marker='*',
                s=100,color='gold')

    if route:
        for i in range(len(route)-2):
            plt.scatter(route[i+1][1],-route[i+1][0],
                        marker=direction[i],color='silver')

    plt.text(end[1],-end[0],'EXIT',color='red',
         horizontalalignment='center',
         verticalalignment='center')
    plt.xticks([])
    plt.yticks([])
    plt.show()

    print(f'Starting point (x, y) = {start[0], start[1]}')
    print(f'Ending point (x, y) = {end[0], end[1]}')
    
    for _, point in enumerate(bonus):
      print(f'Bonus point at position (x, y) = {point[0], point[1]} with point {point[2]}')


def getPathOfMazeFile (fileName):
    temp = os.path.abspath(__file__)
    temp = os.path.dirname(temp)
    temp = os.path.dirname(temp)
    temp = os.path.join(temp,'maze')
    temp = os.path.join(temp, fileName)
    return temp