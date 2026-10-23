import math

print('Число\tКвадратный корень\tКубический корень')
print ('=' * 50)

for i in range(2, 10):
    k = math.sqrt(i)
    k3 = i ** (1/3)
    print(f'{i:>3}\t{k:>15.4f}{k3:>18.4f}')
