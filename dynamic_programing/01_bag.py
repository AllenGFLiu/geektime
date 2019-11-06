# -*- coding:utf-8 -*-
# 01背包动态规划实现代码


def knapsack(weight, w):
    weight_count = len(weight)
    states = [[False for j in range(w+1)] for i in range(weight_count)]  # 用来表示递归树中的节点状态
    states[0][0] = True  # 对第一个元素要特殊对待，在开始循环之前就直接为其赋上正确值
    if weight[0] <= w:
        states[0][weight[0]] = True

    for i in range(1, weight_count):
        for j in range(w+1):  # 表示第i个物品不放入，循环计算所有可能值
            if states[i-1][j] == True:
                states[i][j] = states[i-1][j]

        for j in range(w-weight[i]+1):  # 表示第i个物品放入，同样再循环计算所有可能值
            if states[i-1][j] == True:
                states[i][j+weight[i]] = True

    for i in range(w, -1, -1):
        if states[weight_count-1][i]:
            return i

    return 0


if __name__ == '__main__':
    print(knapsack([2, 2, 4, 6, 3], 9))