
from collections import deque

def melting_bfs(a,b):
    visited[a][b] = True

    # bfs를 수행하면서 즉각적으로 빙산을 녹여버리면 
    # 다음 빙산이 직전에 녹인 빙산을 바다로 착각할 수도 있기에 
    # sea_list에 (x,y,sea(바다와 접한 부분의 갯수))를 저장해두고 마지막에 한꺼번에 녹여준다!
    sea_list = []

    queue = deque()
    queue.append((a,b))

    while queue:
        x,y = queue.popleft()
        
        sea = 0
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
            if n <= nx < 0 or m <= ny < 0 :
                continue

            if graph[nx][ny] == 0:
                sea += 1
            
            elif graph[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))
        if sea > 0:
            sea_list.append((x,y,sea))
    for x,y,sea in sea_list:
        graph[x][y] = max(0,graph[x][y] - sea)

    return 1




n,m = map(int,input().split())
graph = []
year = 0
for _ in range (n):
    graph.append(list(map(int,input().split())))

ice = [] #빙산이 있는 부분의 좌표만 저장
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            ice.append((i,j))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 빙산이 다 녹을 때 까지 수행 
while ice:
    group = 0
    visited =[[False] *m for _ in range(n)]
    del_list = []

    for i,j in ice:
            if graph[i][j] and not visited[i][j]:
                group += melting_bfs(i,j)
            if graph[i][j] == 0:
                del_list.append((i,j))

    if group > 1 :
        print(year)
        break
            
    ice = list(set(ice) - set(del_list))
    year += 1

    
if group < 2:
    print(0)

