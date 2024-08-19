# def say_hello(name): # Принимающая функция
#     print('Hello', name)
# say_hello('Andrei')
# say_hello('Denis')
# say_hello('Max')
# import random
#
#
# def lottery(*args, **kwargs): # Возвращающая функция
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win1 = random.choice(tickets)
#     tickets.remove(win1)
#     win2 = random.choice(tickets)
#     print(*args)
#     return win1, win2
#
# win1, win2 = lottery('mon', 'thue', 'three')
# print(win1, win2)

# def test(a=2, b=True): # Функция с параметрами по умолчанию
#     print(a, b)
# test(False, 'Ok')

# def test(a=2, b=True):
#     print(a, b)
# test(*[1, 2]) # * - распаковка списка, ** - распаковка словаря

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list = []
        matrix.append(list)
        for j in range(m):
            list.append(value)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

