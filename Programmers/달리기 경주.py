# 1. 시간 복잡도 O(players*calling) 솔루션. 데이터 크기 최악일 때 500억 -> 시간 초과 실패
def solution(players, callings):
    for i in range(len(callings)):
        # ** 여기서 시간 초과
        faster = players.index(callings[i]) 
        #교환
        players[faster], players[faster-1] =  players[faster-1], players[faster]
    return players

# 2. 딕셔너리를 이용해 시간복잡도를 O(calling)으로 줄여서 문제 해결
def solution(players, callings):
    # 선수: 등수로 구성된 딕셔너리 생성 - key로 value를 O(1)의 시간복잡도를 이용해 인덱스 탐색
    result = {player:i for i,player in enumerate(players)}
    
    for i in callings:
        idx = result[i] 
        #호명당한 사람 등수 하나 올림
        result[i] -= 1 
        #호명 당한 앞 사람의 등수를 하나 내림
        result[players[idx-1]] += 1 
        # 등수 교환
        players[idx], players[idx-1] = players[idx-1],players[idx]
        
    return players
