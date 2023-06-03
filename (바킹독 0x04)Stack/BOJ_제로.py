import sys
k = int(input())
lists=[]
result = 0
for _ in range(k):
    n = int(sys.stdin.readline().rstrip())
    if n != 0:
        lists.append(n)
    else:
        lists.pop()
    
result = sum(lists)
print(result)

    