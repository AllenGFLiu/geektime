# -*- coding:utf-8 -*-
# 01背包动态规划实现代码
# 動態規劃實現要先從畫出遞歸樹開始,然後逐層遍歷(分階段),對該層出現的重複內容進行合併或者是說使用同一個states狀態來表示即可
# 通過上一層的狀態推出本層對應元素的狀態,是為動態規劃也


"""使用一個二維數組表示遞歸樹中各節點的狀態,比如states[0][2]表示背包在裝第0個物品時重量為2這樣一個狀態,默認為False,可能為True
"""
def knapsack(weight, w):
    weight_count = len(weight)
    states = [[False for j in range(w+1)] for i in range(weight_count)]  # 用来表示递归树中的节点状态
    states[0][0] = True  # 对第一个元素要特殊对待，在开始循环之前就直接为其赋上正确值
    if weight[0] <= w:
        states[0][weight[0]] = True

    for i in range(1, weight_count):  # 對物品分階段處理, 通過上一階段的狀態值動態推導出本輪的狀態值
        for j in range(w+1):  # 表示第i个物品不放入，循环计算所有可能值
            if states[i-1][j]:
                states[i][j] = True

        for j in range(w-weight[i]+1):  # 表示第i个物品放入，同样再循环计算所有可能值
            if states[i-1][j] and not states[i][j+weight[i]]:  # 增加and條件可以減少對相同的狀態做重複的更新動作
                states[i][j+weight[i]] = True

    for i in range(w, -1, -1):
        if states[weight_count-1][i]:
            return i

    return 0


"""使用一個一維數組表示遞歸樹節點狀態
"""
def knapsack2(weight, w):
    n = len(weight)
    states = [False for _ in range(w+1)]
    states[0] = True
    if weight[0] <= w:
        states[weight[0]] = True

    for i in range(1, n):
        for j in range(w-weight[i], -1, -1):  # 這裡不能正序,如果正序操作,前一個更新的元素值會影響後邊元素的判定結果,所以必須倒序遍歷
            if states[j] and not states[j+weight[i]]:
                states[j+weight[i]] = True

    for index in range(w, -1, -1):
        if states[index]:
            return index


if __name__ == '__main__':
    print(knapsack2([2, 2, 4, 6, 3], 9))