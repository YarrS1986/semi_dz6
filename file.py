'''
1. Напишите программу вычисления арифметического выражения заданного строкой.
   Используйте операции +,-,/,*. приоритет операций стандартный.
    2+2 => 4;
    7-8+3*5+1+1+2*3 => 22;

a = '7-82+3*5+13+1+25*3'
b = ['7', '-', '82', '+', '3', '*', '5', '+', '13', '+', '1', '+', '25', '*', '3']
    7, -8, 15, 1, 1, 6
    1-2*3 => -5;
'''

import re

a = '7-8+3*5+1+1+2*3+2'
#print(eval(a))                # проверка верности решения


def calc_multiply(lst, ind):
    sum_mult = lst[ind - 1] * lst[ind + 1]
    for i in range(ind + 2, (len(lst)), 2):
        if lst[i] == "*":
            sum_mult *= lst[i + 1]
        else:
            break
    return sum_mult


def calc_fractional(lst, ind):
    sum_mult = lst[ind - 1] / lst[ind + 1]
    for i in range(ind + 2, (len(lst)), 2):
        if lst[i] == "/":
            sum_mult /= lst[i + 1]
        else:
            break
    return sum_mult


def calc_first_turn(lst):
    lst_app = []
    for i in range(1, len(lst), 2):
        if lst[i] == "*" and lst[i - 2] != "*":
            lst_app.append(calc_multiply(lst, i))
        elif (lst[i] == "*" and lst[i - 2] == "*") or (lst[i] == "/" and lst[i - 2] == "/"):
            continue
        elif lst[i - 2] == "*" or lst[i - 2] == "/":
            lst_app.append(lst[i])
        elif lst[i] == "/" and lst[i - 2] != "/":
            lst_app.append(calc_fractional(lst, i))
        else:
            lst_app.append(lst[i - 1])
            lst_app.append(lst[i])
    if lst[len(lst) - 2] == "+" or lst[len(lst) - 2] == "-":
        lst_app.append(lst[len(lst) - 1])

    return lst_app


nums = re.findall(r'\D+|\d+', a)

if nums[0] == "-":
    nums[1] = float(nums[1]) * -1
    nums.pop(0)
    nums = [float(nums[i]) if i % 2 == 0 else nums[i] for i in range(len(nums))]
elif nums[0] == "+":
    nums.pop(0)
    nums = [float(nums[i]) if i % 2 == 0 else nums[i] for i in range(len(nums))]
else:
    nums = [float(nums[i]) if i % 2 == 0 else nums[i] for i in range(len(nums))]

nums = calc_first_turn(nums)
nums = [nums[i] * -1 if nums[i-1] == "-" else nums[i] for i in range(0, len(nums), 2)]

summary = sum(nums)

print("Для выражения " + a + " ответ: {}".format(round(summary, 2)))