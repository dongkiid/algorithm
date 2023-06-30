def solution(park, routes):
    #이동 방향 정의
    op = {"N":(-1,0), "S":(1,0), "W":(0,-1), "E":(0,1)}
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            # 시작 지점 찾기
            if park[i][j] == 'S':
                x,y = i,j
                # 찾으면 순회 멈춰 주기
                break
    for i in routes:

        direction, step = i.split() # i를 공백 기준으로 나누어서 값을 변수에 할당 (ex.direction = 'N' step = '3')
        
        # 기존 x,y값 복사 해 BFS 수행 (바로 바꿔주면 예외 처리 제대로 안되기 때문) 
        dx, dy = x,y
        
        for i in range(int(step)): 
            nx = x + op[direction][0]
            ny = y + op[direction][1]
            
            if 0 > nx or nx >=len(park) or 0 > ny or ny >= len(park[0]) or park[nx][ny] == 'X':
                x, y = dx, dy
                # 그래프 범위를 벗어나거나, 이동 지점이 X라면 이동 아예 수행 X => x,y 값 변화 없이 순회를 빠져나와 다음 루트로
                break
            else:
                x,y = nx, ny

    return x,y