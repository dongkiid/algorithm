#BOJ, 10807
length = int(input())
lists = list(map(int,input().split()))
num = int(input())
cnt = 0
for i in lists:
    if num == i:
        cnt += 1

print(cnt)
