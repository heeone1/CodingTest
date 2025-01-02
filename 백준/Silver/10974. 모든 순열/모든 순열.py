# 입력 처리
N = int(input())

def dfs(path):
    if len(path) == N:
        print(*path)
        return

    # 사용되지 않은 숫자를 추가
    for i in range(1, N+1):
        if i not in path:
            dfs(path + [i])

dfs([])