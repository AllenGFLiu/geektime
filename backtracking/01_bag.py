# -*- coding:utf-8 -*-
# 01背包:一个背包总的承载重量是Wkg, 把重量不等的n个物品装进背包中。
#  在不超过总承载重量的前提下，让背包中物品的总重量最大
# 贪心算法中物品是可以分割的，但此问题中对每个物品来说只有两个选择,装还是不装,所以叫0-1背包问题
# 面对递归问题时，要时刻注意递归调用是有一个递归栈存在的，去的时候叫递，回来的时候叫堆
#
# bag_value方法是在bag方法的基础上，增加条件：每个物品不仅重量不一，而且价值不一
#  求取在不超过最大重量的前提下，让背包中物品的总价值最大
tmp_weight = 0  # 全局变量，用来存储bag实际存储的最大重量



def bag(i, cw, n_weight, bag_max_weight):
    if cw == bag_max_weight or i == len(n_weight):  # 递归终止条件
        global tmp_weight
        if cw > tmp_weight:
            tmp_weight = cw
        return
    
    bag(i+1, cw, n_weight, bag_max_weight)  # 递推公式:从第一个物品开始，选择不装入背包，依次递归
                                            # 一直到最后一个物品，触发递归终止条件，然后返回，就可以执行此行之后的函数了

    if cw+n_weight[i] <= bag_max_weight:
        # 判断当前重量再加上本物品的重量如果不超过背包最大重量，就可以把本物品装入背包中
        bag(i+1, cw+n_weight[i], n_weight, bag_max_weight)  # 这是装入物品调用的递归

tmp_value = 0  #同tmp_weight,用来存储物品最大的价值和

def bag_value(i, cw, cv, n_weight, n_value, bag_max_weight):
    if cw == bag_max_weight or i == len(n_weight):
        global tmp_value
        if cv > tmp_value:
            tmp_value = cv
        return

    bag_value(i+1, cw, cv, n_weight, n_value, bag_max_weight)

    if cw+n_weight[i] <= bag_max_weight:
        bag_value(i+1, cw+n_weight[i], cv+n_value[i], n_weight, n_value, bag_max_weight)


if __name__ == '__main__':
    n_weight = [2, 1, 4, 8, 3]
    n_value = [5, 2, 10, 1, 6]
    max_weight = 8
    bag_value(0, 0, 0, n_weight, n_value, max_weight)
    print(tmp_value)