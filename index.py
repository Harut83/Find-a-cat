n = int(input())
flag = False
for i in range(n):
    word = input()
    if 'cat' in word or 'Cat' in word:
        flag = True
if flag:
    print('MEOW')
else:
    print('NO')