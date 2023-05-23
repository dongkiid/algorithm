#mCn으로 해결하는 조합 문제 
# factorial 함수를 직접 만들어 해결 
# math 모듈을 임포트해서 math.factorial(n)을 사용하는 방법도 있음

def factorial(n):
    num = 1
    for i in range(1,n+1):
        num *= i
    return num

n = int(input())

for _ in range(n):
    N,M = map(int,input().split())
    result = factorial(M) // (factorial(N) * factorial(M-N))
    print(result)