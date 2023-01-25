#太郎持っているカード
taro_cards = [[False for i in range(1, 14)] for j in range(4)]
#絵柄を定義
pattern = ['S', 'H', 'C', 'D']

n = int(input())
#cards[i][j] の状態を記録
for i in range(n):
    mark, rank = input().split()
    rank = int(rank)
    taro_cards[pattern.index(mark)][rank-1] = True
#cards[i][j] が False のカードを順番に出力
#i を 0 から 3 、 j を 0 から 12 まで回す2重ループで出力
for i in range(4):
    for j in range(13):
        if taro_cards[i][j] == False:
            print(pattern[i], j+1)
