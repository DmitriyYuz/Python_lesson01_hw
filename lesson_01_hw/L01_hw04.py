
x = int(input('Введите число: '))
max = 0
min = 9
while x > 0:
    last = x % 10
    if last > max:
        max = last
    if last < min:
        min = last
    x=x//10

print('Самая большая цифра в цисле: ', max)
print('Самая маленькая цифра в цисле: ', min)
