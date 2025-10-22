n = int(input())
two = 0
while n > 1 :
    if n % 2 == 0:
        n = n // 2
        two += 1 
    else:
        break


print(n, two)