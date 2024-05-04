num = input().split()
for i in range(len(num)):
    cnt=1
    for j in range(len(num)):
        if num[i]==num[j]:
            cnt+=1