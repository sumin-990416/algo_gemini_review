n = int(input())
home = list(map(int,input().split()))
away = list(map(int,input().split()))

result = 0
for i in range(n):
    if home[i] > away[i]:
        result += 3
    elif home[i] == away[i]:
        result += 1
    else:
        result += 0

print(result)