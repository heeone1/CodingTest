N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

path = []

def dfs(n, list):
    if n == M:
        path.append(list)
        return
    
    for i in range(N):
        dfs(n+1, list+[numbers[i]])

dfs(0, [])

for list in path:
    print(*list)