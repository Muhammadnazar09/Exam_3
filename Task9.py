ket = input().split()
kar = int(input())
cnt=1
for i in range(len(ket)):
    if kar<=int(ket[i]):
        cnt+=1
print(cnt)