from collections import deque
import sys

def grouping(n,k):

    queue = deque()
    queue.append((n,k))
    visited[n][k] = 1
    graph[n][k] = group_id

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= N or ny >= N or nx < 0 or ny < 0:
                continue

            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx,ny))
                visited[nx][ny] = 1
                graph[nx][ny] = group_id
            
def minimum_route(z):

    global route
    dist =[[0]* N for _ in range(N)] #이동 횟수를 정확히 카운트 하기 위해 -1로 초기화 
    queue = deque()
    
    for i in range(N):
        for j in range(N):
            # 그룹이 같은 곳들은 섬을 잇는 최단 거리 카운트에서 제외하기 위해 미리 방문처리를 해준다.
            if z == graph[i][j]:
                queue.append((i,j))
                dist[i][j] = 1    
    #print(queue)
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= N or ny >= N or nx < 0 or ny < 0:
                continue

            #바다이면서 지나가지 않은 지점
            if graph[nx][ny] == 0 and dist[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx,ny))
            #바다가 아니면서 지나가지 않은 지점
            if graph[nx][ny] != 0 and graph[nx][ny] != z and dist[nx][ny] == 0:
                route = min(route,dist[x][y]-1)
                return


                

N = int(input())
graph = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))
group_id = 1 
route = 10001 #임의로 설정해둔 최고 숫자
for i in range(N):
    for j in range(N):
        visited=[[0] * N for _ in range(N)]
        if graph[i][j] == 1 and visited[i][j] == 0:
            grouping(i,j)
            group_id += 1
            print(graph)

#print(graph)

for i in range(2,group_id):
    minimum_route(i)

print(route)


#------- 백준에서 발견한 런타임 훨씬 줄이는 로직 (위에 코드는 2200~2300 ms.. 원래였으면 시간초과여야함) => 300ms 정도로 줄일 수 있음) 
#---------- border 배열 생성하여 섬 외곽의 지점들을 모두 저장한 뒤 다른 섬과의 최단거리를 구하고 그 중 가장 짧은 방식을 선택하는 방법. 
#---------- 최단 거리 구할 때 border배열안에 요소만으로 방문을 수행하기 때문에 시간이 줄임

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
maps = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*(N) for _ in range(N)]
border = []
ways = [[0,1],[1,0],[-1,0],[0,-1]]
answer = N*N

def changeMaps(x,y,irelandNum):
    borderTmp = []
    queue = deque()
    queue.append([x,y])
    
    while queue:
        x, y = queue.popleft()
        maps[x][y] = irelandNum
        tmpCnt = 0
        
        for i in range(4):
            nx, ny = x+ways[i][0], y+ways[i][1]
            
            if 0 <= nx < N and 0 <= ny < N:
                if not maps[nx][ny]:
                    tmpCnt =+ 1
                if not visited[nx][ny] and maps[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append([nx,ny])
                    
        if tmpCnt:
            borderTmp.append([x,y])

    return borderTmp

irelandNum = 1
for i in range(N):
    for j in range(N):
        if maps[i][j] and not visited[i][j]:
            border.append(changeMaps(i,j,irelandNum))
            irelandNum += 1

def minDistance(borderList, curr_Ireland):
    result = N*N
    visited = [[0]*(N) for _ in range(N)]
    queue = deque()
    
    for x in borderList:
        queue.append(x)
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x+ways[i][0], y+ways[i][1]
            
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and not maps[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx,ny])
                if maps[nx][ny] > curr_Ireland and result > visited[x][y]:
                    result = visited[x][y]
                    return result

for i in range(len(border)-1):
    answer = min(answer, minDistance(border[i],i+1))

print(answer)
