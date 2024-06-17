result = 0
candy = int(input())
for A in range(0,candy+1):
    for B in range(0,candy+1):
        for C in range(0,candy+1):
            if A + B + C == candy:
                if A!= 0 and B != 0 and C !=0:
                    if A >= B + 2:
                        if C % 2 == 0:
                            result += 1  

 
print(result)
            

