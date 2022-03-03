from general import*
from os import*
from DepthFirstSearch import*
from AStarSearch import*
from BreadthFirstSearch import*
from GreedyBestFirstSearch import*


menuOptionsAlgorithm = {
    1: 'Thuat toan tim kiem DFS (Depth First Search)',
    2: 'Thuat toan tim kiem BFS',
    3: 'Thuat toan tim kiem tham lam (Greedy Best First Search)',
    4: 'Thuat toan tim kiem A*',
    5: 'Thoat'
}

menuOptionsTypeMap = {
    1: 'Ban do khong co diem thuong',
    2: 'Ban do co diem thuong',
    3: 'Thoat'
}

menuOptionsNormalMap = {
    1: 'Ban do so 1',
    2: 'Ban do so 2',
    3: 'Ban do so 3',
    4: 'Ban do so 4',
    5: 'Ban do so 5',
    6: 'Thoat'
}

menuOptionsBonusMap = {
    1: 'Ban do co 2 diem thuong',
    2: 'Ban do co 5 diem thuong',
    3: 'Ban do co 10 diem thuong',
    4: 'Thoat'
}

# clear screen
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def printMenu(menuOptions):
    for key in menuOptions.keys():
        print (key, '--', menuOptions[key] )

def selectMenu(menuOptions):
    clear()
    n = len(menuOptions)
    printMenu(menuOptions)
    option = ''
    try:
        option = int(input('Lua chon cua ban: '))
    except:
        option = 'Du lieu dau vao khong hop le. Vui long nhap so nguyen...'
    return option

def runAlgorithms(algorithms, map, bonus=False):
    if bonus == True:
        if map == 1:
            matrix, bonus_points, graph, start, end = read_file(getPathOfMazeFile(f'maze_map_2_bonus.txt'))
        elif map == 2:
            matrix, bonus_points, graph, start, end = read_file(getPathOfMazeFile(f'maze_map_5_bonus.txt'))
        elif map == 3: 
            matrix, bonus_points, graph, start, end = read_file(getPathOfMazeFile(f'maze_map_10_bonus.txt'))
        route = AStarSearch(graph, start, end, bonus)        
        if(route == False or route == []):
            clear()
            print('Khong tim ra duong di....')
        else: 
            print(f'Quang duong: {lengthOfRoute(route, bonus)}')
            visualize_maze(matrix,bonus_points,start,end,route)

    else:
        matrix, bonus_points, graph, start, end = read_file(getPathOfMazeFile(f'maze_map{map}.txt'))
        print(f'The height of the matrix: {len(matrix)}')
        print(f'The width of the matrix: {len(matrix[0])}')
        route = []
        if(algorithms == 1):
            route = DFSearch(graph,start,end)
        elif (algorithms == 2):
            route = BFSearch(graph,start,end)
        elif (algorithms == 3):
            route = GBFSearch(graph,start,end)
        elif (algorithms == 4):
            route = AStarSearch(graph,start,end)
        if(route == False or route == []):
            clear()
            print('Khong tim ra duong di....')
        else: 
            print(f'Quang duong: {lengthOfRoute(route)}')
            visualize_maze(matrix,bonus_points,start,end,route)

if __name__=='__main__':
    while(True):
        clear()
        # Chon thuat toan
        algor = selectMenu(menuOptionsAlgorithm)
        if type(algor) == 'string':
            print(algor)
            system('pause')
        ## Chon 3 thuat toan dau tien
        elif algor == 1 or algor == 2 or algor == 3:
            while(True):
                clear()
                ### Chon ban do
                map = selectMenu(menuOptionsNormalMap)
                if type(map) == 'string':
                    print(map)
                    system('pause')
                elif map == 1 or map == 2 or map == 3 or map == 4 or map ==5:
                    runAlgorithms(algor,map)
                    system('pause')
                elif map == 6:
                    break
                else:
                    print('Vui long nhap mot so tu 1 den 6...')
                    system('pause')
        # Nguoi dung chon thuat toan tim kiem A*            
        elif algor == 4:
            while (True):
                clear()
                typeMap = selectMenu(menuOptionsTypeMap)
                if type(typeMap) == 'string':
                    print(typeMap)
                    system('pause')
                # Truong hop map khong co diem thuong
                if typeMap == 1:
                    while(True):
                        clear()
                        map = selectMenu(menuOptionsNormalMap)
                        if map == 1 or map == 2 or map == 3 or map == 4 or map ==5:
                            runAlgorithms(algor,map)
                            system('pause')
                        elif map == 6:
                            break
                        else:
                            print('Vui long nhap mot so tu 1 den 6...')
                            system('pause')
                #Truong hop map co diem thuong
                elif typeMap == 2:
                    while(True):
                        clear()
                        ### Chon 1 trong 3 ban do co diem thuong
                        map = selectMenu(menuOptionsBonusMap)
                        if type(map) == 'string':
                            print(map)
                            system('pause')
                        elif map == 1 or map == 2 or map == 3:
                            runAlgorithms(algor,map,True)
                            system('pause')
                        elif map == 4:
                            break
                        else:
                            print('Vui long nhap mot so tu 1 den 4...')
                            system('pause')
                elif typeMap == 3:
                    break
                else:
                    print('Vui long nhap mot so tu 1 den 3...')
                    system('pause')
        elif algor == 5:
            exit()
        else:
            print('Vui long nhap mot so tu 1 den 5...')
            system('pause')
