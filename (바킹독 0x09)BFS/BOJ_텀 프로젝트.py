import sys
sys.setrecursionlimit(1000000) #재귀 깊이 설정

def dfs(i):
    global team_member

    visited[i] = True #방문 처리
    team.append(i) # 나부터 팀 후보에 추가
    nxt_student = arr[i] # 다음 사람 지목

    if visited[nxt_student] : # 지목한 사람이 이미 방문처리 되었고
        if nxt_student in team: # 그 사람이 team에 있다면
            team_member += len(team[team.index(nxt_student):]) # team 결성! (team 안에 nxt_student가 첫 등장하는 인덱스부터 끝 요소까지의 길이를 반환해 team_member에 저장)
    else:
        dfs(nxt_student) # 지목받은 사람 -> 다른 사람 지목
        
    
N = int(input())

for _ in range(N):
    team_member = 0
    students = int(input())
    arr = [0]+list(map(int,input().split()))
    visited = [False for _ in range(students+1)]
    
    for i in range(1,students+1):
        if not visited[i]:
            team = []
            dfs(i)
    
    print(students - team_member) 

    