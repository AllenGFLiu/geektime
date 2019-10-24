# -*- coding:utf-8 -*-
# 八皇后：8X8的棋盘,希望往其中放入8个棋子(皇后),每个棋子所在的行/列/对角线都不能有另一个棋子.
# 回溯算法就是枚举搜索，适合使用递归实现。
# debug八皇后代码时，要意识到递归栈的存在，就可以理解回溯算法中所谓的回溯的含义


queens = [-1]*8  # 下标表示棋子所在的行，保存的元素值表示棋子所在的列，通过行和列定位棋子在棋盘中的位置
                 #  8个元素就代表8个棋子分别存在的行和列


def print_queens(queens):
    # 使用两个for循环，打印所有棋盘的布局可能
    for i in range(8):
        for j in range(8):
            if queens[i] == j:
                print('Q ', end=' ')
            else:
                print('* ', end=' ')
        print()
    print()


def is_ok(row, column):
    global queens
    leftup = column - 1  # 当前所在位置对角线左上的位置
    rightup = column + 1  # 当前所在位置对角线右上的位置
    for i in range(row - 1, -1, -1):  # 从当前所在的row行的上一行逐行往上去查，看是否有重合
        if queens[i] == column: return False
        if leftup >= 0:
            if queens[i] == leftup:
                return False
        if rightup <= 8:
            if queens[i] == rightup:
                return False
        leftup -= 1
        rightup += 1
    return True



def cal_queens(row):
    global queens
    if row == 8:
        print_queens(queens)
        return
    
    for column in range(8):
        if is_ok(row, column):
            queens[row] = column
            cal_queens(row+1)  # 本行符合条件，递归调用下一行，再重新range(8),从第0列开始放置棋子


if __name__ == '__main__':
    cal_queens(0)
    