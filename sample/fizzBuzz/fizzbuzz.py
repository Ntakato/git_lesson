n = int(input ('input number\n'))
print('-----')

for i in range(1, n+1):
    if i % 3 == 0:
        print('Fiz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
