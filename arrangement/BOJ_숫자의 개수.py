a = int(input())
b = int(input())
c = int(input())
num = str(a*b*c)
#print(num)
result = [0]*10
for i in num:
    result[int(i)] += 1
for j in result:
    print(j)