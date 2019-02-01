# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    a, b = 1, 1
    f_list = [1, ]

    for i in range(m):
        a, b = b, a + b
        f_list.append(a)

    return f_list[n - 1:m]


print('fibonacci(1, 6): ', fibonacci(1, 6))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    if len(origin_list) > 1:
        pivot_index = len(origin_list) // 2
        smaller_items = []
        larger_items = []

        for i, val in enumerate(origin_list):
            if i != pivot_index:
                if val < origin_list[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)

        sort_to_max(smaller_items)
        sort_to_max(larger_items)
        origin_list[:] = smaller_items + [origin_list[pivot_index]] + larger_items

    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def filter_func(function, iterable):
    return (item for item in iterable if function(item))


print(list(filter_func(lambda x: True if x % 2 == 0 else False,
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
def is_parallelogram(a1, a2, a3, a4):
    if abs(a3[0] - a2[0]) == abs(a4[0] - a1[0]) and \
            abs(a2[1] - a1[1]) == abs(a3[1] - a4[1]):
        return True
    return False
