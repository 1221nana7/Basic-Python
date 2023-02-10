count = [0] * 26
while True:
    try:
        lines=input().lower()
    except:
        break
    for n in lines:
        if 'a'<=n and n<='z':
            count[ord(n)-ord("a")]+=1

for i in range(26):
    print(chr(ord("a")+i),":",count[i])
