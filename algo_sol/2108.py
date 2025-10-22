n = int(input())

list_num = []

for i in range(n):
    list_num.append(int(input()))
list_num.sort()

list_dict = {}

for i in range(n):
    list_dict[list_num[i]] = 0

for i in range(n):
    list_dict[list_num[i]] += 1

max_num = max(list_dict.values())
num_list = []
for key, value in list_dict.items():
    if value == max_num:
        num_list.append(key)




print(int(round((sum(list_num)/n))))
print(list_num[n//2])
if len(num_list) == 1:
    print(num_list[0])
else:
    print(num_list[1])
print(list_num[-1] - list_num[0])
