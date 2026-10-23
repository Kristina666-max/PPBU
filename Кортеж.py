import random

for i in range(10):
    a1 = str(random.randint(0,99))
    a2 = str(random.randint(0,999))
    a3 = str(random.randint(0,9999))        
    print(f'| {a1:>4} | {a2:>4} |\t {a3:>4} |\t')
