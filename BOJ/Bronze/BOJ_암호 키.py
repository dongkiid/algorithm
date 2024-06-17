N=int(input())
for _ in range(N):
    number = int(input())
    for i in range( 2, 1000001):
        if number % i == 0: # 1,000,000 이하의 소인수가 하나라도 있으면
            print("NO")
            break
        if i == 1000000: # 위 조건이 맞지 않아 1,000,000까지 i가 도달했다면 == 1,000,000 이하 소인수 없다는 뜻
            print("YES")
