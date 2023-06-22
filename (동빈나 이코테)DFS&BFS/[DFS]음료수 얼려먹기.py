def dfs(x,y):
    if x <= -1 or y <= -1 or x >=n or y >= m:
        return False

    if graph[x][y] == 0:
        #해당 지점 방문 처리
        graph[x][y] = 1
        #주변 지점 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y) # 좌
        dfs(x + 1,y) # 우
        dfs(x,y + 1) # 상
        dfs(x, y - 1) #하
        return True
    return False

n,m = map(int,input().split())

#2차원 리스트에 맵정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

#모든 지점에 대해 음료수를 채워나가 보자
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
print(result)
