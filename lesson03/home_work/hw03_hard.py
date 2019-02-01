# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

user_input = '-2/3 - -2'


def nod(a, b):
    '''
    Нахождение наибольшего общего
    делителя
    '''
    while b:
        a, b = b, a % b
    return a


def formatout(num):
    '''
    форматирование строки ответа
    '''
    if type(num) is int:
        return num

    if len(num) == 2:
        res = '%s/%s' % (num[0], num[1])

    if len(num) == 3:
        res = '%s %s/%s' % (num[0], num[1], num[2])

    return res


def defract(num):
    '''
    выделение целой части из дроби
    '''
    if not num[0] % num[1]:
        res = int(num[0] / num[1])

    elif abs(num[0]) > abs(num[1]):
        res = [int(num[0] / num[1]), abs(num[0]) % num[1], num[1]]

        n = nod(abs(res[1]), abs(res[2]))
        if n != 1:
            res[1], res[2] = int(res[1] / n), int(res[2] / n)
    else:
        res = num

        n = nod(abs(res[0]), abs(res[1]))
        if n != 1:
            res[0], res[1] = int(res[0] / n), int(res[1] / n)

    return res


def fract(num):
    '''
    приведение к дроби
    '''
    if num[0] and num[2]:
        num[1] = (num[0] * num[2] + num[1] if num[0] > 0 else
                  num[0] * num[2] - num[1])
        num[0] = False

    return [n for n in num if n]


def calcfract(*n):
    '''
    вычисление дробей и целых чисел
    '''
    if len(n) == 3:
        sign = n[len(n) - 1]
        num1 = fract([n[0]['int'], n[0]['num'], n[0]['dem']])
        num2 = fract([n[1]['int'], n[1]['num'], n[1]['dem']])

        if len(num1) == len(num2):
            if len(num1) == 1:
                res = (num1[0] + num2[0] if sign == '+' else
                       num1[0] - num2[0])
            if len(num1) == 2:
                group = list(zip(num1, num2))
                if group[1][0] == group[1][1]:
                    res = (sum(group[0]) if sign == '+' else
                           group[0][0] - group[0][1])
                    res = [res, group[1][0]]
                else:
                    res = (group[0][0] * group[1][1] +
                           group[0][1] * group[1][0] if sign == '+' else
                           group[0][0] * group[1][1] -
                           group[0][1] * group[1][0])
                    res = [res, group[1][0] * group[1][1]]

        else:
            if sign == '+':
                res = ([num1[0] * num2[1] + num2[0], num2[1]] if
                       len(num1) == 1 else
                       [num2[0] * num1[1] + num1[0], num1[1]])
            if sign == '-':
                res = ([num1[0] * num2[1] - num2[0], num2[1]] if
                       len(num1) == 1 else
                       [-(num2[0] * num1[1] - num1[0]), num1[1]])

    if len(n) == 1:
        res = fract([n[0]['int'], n[0]['num'], n[0]['dem']])
        if len(res) == 1:
            res = res[0]

    if not type(res) is int:
        res = defract(res)
        res = formatout(res)

    print('Ответ: %s' % (res))
    return res


def discharge(li):
    '''
    выделение числителя, знаменателя
    и целой части
    '''
    # int: целая часть
    # num: числитель
    # dem: знаменатель

    num = {'int': False, 'num': False, 'dem': False}

    if len(li) == 1:
        num['int'] = int(li[0])

    if len(li) == 2 and ~li[1].find('/'):
        num['int'] = int(li[0])
        num['num'] = int(li[1].split('/')[0])
        num['dem'] = int(li[1].split('/')[1])

    if len(li) == 2 and li[1].isdigit():
        num['num'] = int(li[0])
        num['dem'] = int(li[1])

    return num


def formatin(usr_in):
    '''
    форматирование входной строки
    '''
    usr_in = usr_in.strip()

    is_one_operand = False
    sign = False

    plus = usr_in.find(' + ')
    minus = usr_in.find(' - ')

    if not ~minus and not ~plus:
        is_one_operand = True
    else:
        sign = usr_in[minus + 1] if ~minus else usr_in[plus + 1]

    print('Выражение: %s' % (usr_in))

    if is_one_operand:
        oper = (usr_in.split(' ') if ~usr_in.find(' ') else
                usr_in.split('/'))
        num = discharge(oper)
        return calcfract(num)
    else:
        opers = usr_in.split(' ' + sign + ' ')
        oper1 = (opers[0].split(' ') if ~opers[0].find(' ') else
                 opers[0].split('/'))
        oper2 = (opers[1].split(' ') if ~opers[1].find(' ') else
                 opers[1].split('/'))
        num1 = discharge(oper1)
        num2 = discharge(oper2)
        return calcfract(num1, num2, sign)


formatin(user_input)

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
