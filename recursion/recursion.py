# 遞歸:
# 寫出遞歸公式,找到終止條件
# 推到遞歸公式時,假設子問題已經解決,在此基礎上思考如何解決父問題,避免人腦思考遞歸細節.
#
# 使用遞歸要注意堆棧溢出,還有重複計算
# Author: AllenGFLiu
# #####################################################


def fib(n):
    '''斐波那契數列
    '''
    if n == 1:
        return 1
    if n == 2:
        return 1

    return fib(n-1) + fib(n-2)


def factorial(n):
    '''階乘
    '''
    if n == 0:
        return 1
    return n * factorial(n-1)


def permutate(l):
    '''全排列
    '''
        


if __name__ == '__main__':
    print(fib(5))
    print(factorial(5))