def solution(arr):
    mini = min(arr)
    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(mini)
        return arr
            
        