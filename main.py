# TODO: 使用01编码阴阳爻
# TODO: 找到阴阳爻的字符
# TODO: 完成变卦的编写
# TODO: 适配周易64卦的编码和字符集
# TODO: 学习起卦、纳甲、安适应、寻卦宫、装六亲、解卦

import random


def random_return_two_or_three():
    return random.choice([2, 3])


def get_xx():
    a = random_return_two_or_three()
    b = random_return_two_or_three()
    c = random_return_two_or_three()
    xx = a + b + c
    return xx


def get_ben():
    xxs = []
    for i in range(6):
        xxs.append(get_xx())

    xxs_reverse = xxs[::-1]
    return xxs_reverse


def print_xx(num):
    if num == 9:
        print("-o")
    elif num == 6:
        print("--x")
    elif num % 2 == 1:
        print("-")
    elif num % 2 == 0:
        print("--")


list_a = get_ben()
for i in range(len(list_a)):
    print_xx(list_a[i])
