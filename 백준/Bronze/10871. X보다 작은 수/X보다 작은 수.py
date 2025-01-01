N, X = map(int, input().split())

numbers = list(map(int, input().split()))

result = []

for i in range (0, len(numbers)):
    if numbers[i]<X:
        result.append(numbers[i])

print(" ".join(map(str, result)))