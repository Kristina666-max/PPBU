def summator(a=10, b=4):
    # print(a + b)
    return a * b


def printing(*args, **kwargs):
    print(args)
    print(kwargs)
    # return sum(args)



# n = 45
# cc = 'qwerty'
# n = summator(2, 3)
# # n = summator(2)
# print('функция', n)
# print(summator(2))  # позиционные аргументы
# print(summator())
# print(summator(b=8))  # Ключевые аргументы

print(printing())
print(printing(1, 3, nn=16, y=45))
printing('Name1', 'Name2', 'Name3')
printing('Name1', 'Name2')