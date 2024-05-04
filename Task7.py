number = input().split()
num = int(input())
for i in range(len(number)):
    if i==num:
        continue
    print(number[i],end=" ")