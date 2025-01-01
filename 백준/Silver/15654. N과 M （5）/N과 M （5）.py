# 입력 받기
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 숫자 정렬 (사전 순 출력 위해)
numbers.sort()

# 현재 수열을 저장하는 리스트
path = []

def backtrack(depth):
    if depth == M:
        print(" ".join(map(str, path)))
        return
    for num in numbers:
        if num not in path:  # 중복 선택 방지
            path.append(num)
            backtrack(depth + 1)
            path.pop()

backtrack(0)
