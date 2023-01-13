a,b,c = map(int, input().split())
x = 0
for y in range(a, b+1):
    if c % y ==0:
        x+=1
print(x)
