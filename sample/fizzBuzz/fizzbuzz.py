num1, str1 = input ('input number, string\n').split()
num2, str2 = input().split()
print ('-----')

num1 = int(num1)
num2 = int(num2)

for i in range(1, 101):
    if i % int(num1) == 0:
        print(str1)
    elif i % int(num2) == 0:
        print(str2)
    else:
        print(i)
