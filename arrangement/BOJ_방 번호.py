#BOJ, 1475
#6,9는 서로 뒤집어서 사용할 수 있다는 점이 포인트
room_number = input()
num_set = [0]*10
cnt = 0

for i in room_number:
    num = int(i)

    if num == 9:
        num = 6

    num_set[num] += 1

dupl = int(num_set[6] / 2)
if num_set[6] % 2 ==0:
    num_set[6] = dupl
else:
    num_set[6] = dupl+1

print(max(num_set))