# Find-a-cat
Write a program that finds the cat. The user enters first the number of lines, then the lines themselves. If at least one entered line contains a combination of the letters "Cat" or "cat", the program displays "MEOW", otherwise the program displays "NO".
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
