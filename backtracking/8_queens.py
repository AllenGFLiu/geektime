queens = [-1]*8


def print_queens(queens):
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
    for i in range(row - 1, -1, -1):
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
            cal_queens(row+1)


if __name__ == '__main__':
    cal_queens(0)
    