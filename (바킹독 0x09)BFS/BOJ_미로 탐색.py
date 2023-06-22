#동빈나 미로 탈출이랑 로직 동일

from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 현재 위치로부터 상,하,좌,우 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1: # 해당 노드를 처음 방문하는 경우에만 기록
                graph[nx][ny] = graph[x][y] + 1 # 이전 노드의 값에 +1 한 값을 저장
                queue.append((nx, ny))
    # 가장 오른쪽 아래 값 (=최단 거리)를 반환
    return graph[n - 1][m - 1]

n, m = map(int, input().split())
graph = [list(map(int,input())) for _ in range(n)]

# 입력 값을 그래프 형태로 저장한 graph 배열은 
# 아래의 코드로 생성한 graph와 동일한 값을 가질 수 있는데

# graph = []
# for i in range(n):
#    graph.append(list(map(int, input())))

# 배열 생성 후 for문을 새로 만드는 것 보다 
# 배열 생성시 for문을 넣어주는 게 미묘한 차이로 더 속도가 빠르다. 


# 이동 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))