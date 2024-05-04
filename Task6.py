num = input().split()
for i in range(len(num)):
    for j in range(len(num)):
        if num[i]!=num[j]:
            print(num[j],end="")