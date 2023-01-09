'''
2. Добавьте возможность использования скобок, меняющих приоритет операций.

    1+2*3 => 7;
    (1+2)*3 => 9;
'''


import re

# a = "(1+2)*3"
a = '-7-82+(((3*5+13)+1)+25*(3/5+8)-6)'
# print(eval(a))                # проверка верности решения


def calc_multiply(lst, ind):
    sum_mult = lst[ind - 1] * lst[ind + 1]
    for i in range(ind + 2, (len(lst)), 2):
        if lst[i] == "*":
            sum_mult *= lst[i + 1]
        else:
            break
    return sum_mult


def calc_fractional(lst, ind):
    sum_frac = lst[ind - 1] / lst[ind + 1]
    for i in range(ind + 2, (len(lst)), 2):
        if lst[i] == "/":
            sum_frac /= lst[i + 1]
        else:
            break
    return sum_frac


def calculate_management(lst):
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
    lst_app = [lst_app[i] * -1 if lst_app[i - 1] == "-" else lst_app[i] for i in range(0, len(lst_app), 2)]
    summary = sum(lst_app)
    print(summary)
    return summary


def find_list_in_brackets(lst, ind):
    lst_in_brackets = []
    for i in range(ind + 1, len(lst)):
        if lst[i] != ")":
            lst_in_brackets.append(lst[i])
        else:
            break
    return calculate_management(lst_in_brackets)


def list_without_brackets(lst, open_br, close_br):
    list_br = []
    val = find_list_in_brackets(lst, open_br)
    for i in range(len(lst)):
        if open_br < i <= close_br:
            continue
        elif i == open_br:
            list_br.append(val)
        else:
             list_br.append(lst[i])
    print(list_br)
    return check_for_brackets(list_br)


def check_for_brackets(lst):
    open_br = 0
    close_br = 0
    for i in range(len(lst)):
        if lst[i] == "(":
            open_br = i
            for j in range(open_br, len(lst)):
                if lst[j] == ")":
                    close_br = j
                    break
        elif "(" not in lst:
            return lst
    list_without_brackets(lst, open_br, close_br)


nums = re.findall(r'[+)(*/]|\D+|\d+', a)

if nums[0] == "-":
    nums[1] = float(nums[1]) * -1
    nums.pop(0)
    nums = [nums[0]] + [float(nums[i]) if nums[i].isdigit() else nums[i] for i in range(1, len(nums))]
elif nums[0] == "+":
    nums.pop(0)
    nums = [float(nums[0])] + [float(nums[i]) if nums[i].isdigit() else nums[i] for i in range(1, len(nums))]
else:
    nums = [float(nums[i]) if nums[i].isdigit() else nums[i] for i in range(len(nums))]
print(nums)

check_for_brackets(nums)

# nums = [nums[i] * -1 if nums[i - 1] == "-" else nums[i] for i in range(0, len(nums), 2)]
# summary = sum(nums)
# print(summary)

