#10部屋3階建て4棟
house = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
#情報の数 n
n = int(input())
#n 件の情報,情報には４つの整数 b, f, r, v が空白区切りで１行
for i in range(n):
    b,f,r,v = map(int, input().split())
    house[b-1][f-1][r-1] += v

for b in range(4):
    for f in house[b]:
       print("", *f)
    if b == 3:
        break
    print("#" * 20)
