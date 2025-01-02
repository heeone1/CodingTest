from itertools import permutations

N = int(input()) 

list = list(map(int, input().split()))

list2 = []
max_value = 0

def result(max_value):
    for perm in permutations(list):
        num = 0
        for i in range(N-1):
            num += abs(perm[i] - perm[i+1])
        
        max_value = max(max_value, num)
    
    return max_value

answer = result(max_value)    

print(answer)