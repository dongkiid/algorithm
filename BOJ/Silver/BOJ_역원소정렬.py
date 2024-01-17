import sys
input = sys.stdin.readline

# *을 붙여서 변수를 선언해주면 정해지지 않은 개수의 입력값을 받을 수 있다.
n, *num = input().split()

while len(num) < int(n):
  num.extend(input().split())

for i in range(int(n)):
    num[i] = num[i][::-1]

num = sorted(list(map(int, num)))
print(*num, sep="\n")