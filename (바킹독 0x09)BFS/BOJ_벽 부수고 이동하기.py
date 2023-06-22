
from collections import deque
def bfs(a,b):
    queue = deque()
    queue.append((a,b,0))
    visited[a][b][0] = 1

    while queue:
        x,y,z = queue.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or nx >= N or 0 > ny or ny >= M or visited[nx][ny][z] != 0:
                continue

            if graph[nx][ny] == 1 and z == 0: # 부순 적 없는 벽인 경우 -> 부시고 break count 1
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx,ny,1))

            if graph[nx][ny]== 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx,ny,z))
    return -1
                

N, M = map(int,input().split())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


graph =[list(map(int,input())) for _ in range(N)]

# N,M이 최대 1000 입력 받을 수 있으므로 
# 2차원 배열로 visited 그래프를 구성하면, 벽 부시기 가능 여부를 위치마다 한번씩 더 확인해야하므로 시간 복잡도가 O(NM^2) = 1조 => 시간 초과
# 따라서 3차원 배열을 활용해서 문제를 풀어야 함 (시간 복잡도 = O(NM) = 백만) 
# 방문처리 = visited[x][y][z] = 1
# visited[x][y][0] = 벽 안 부수고 가는 경로
# visited[x][y][1] = 벽 부수고 경로
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

print(bfs(0,0))
