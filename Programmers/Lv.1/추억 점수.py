def solution(name, yearning, photo):
    lists = dict(zip(name, yearning)) #zip() = iterable한 객체를 묶어서 새로운 iterable 객체로 반환
    answer = []

    for i in range(len(photo)):
        cnt = 0
        for j in range(len(photo[i])):
            if photo[i][j] in lists: # 키로 찾고
                cnt += lists[photo[i][j]] # 키의 값을 누적 합산
        answer.append(cnt)
    
    return answer