N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

path = []

def backtrack(depth):
    if len(path) == M:
        print(" ".join(map(str, path)))
        return
    for num in range(depth, N):
        path.append(numbers[num])
        backtrack(num + 1)
        path.pop()

backtrack(0)