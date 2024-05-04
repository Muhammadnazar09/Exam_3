num = input().split()
for i in range(1,len(num)):
    if int(num[i-1])>0 and int(num[i])>0 or int(num[i-1])<0 and int(num[i])<0:
        print(num[i-1],num[i])
        break