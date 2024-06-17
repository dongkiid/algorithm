import sys
N = int(sys.stdin.readline())
arr = []

for i in range(N):
    arr.append(sys.stdin.readline().strip())

arr = list(set(arr))
arr.sort()
arr.sort(key=len)

print(*arr,sep="\n")
