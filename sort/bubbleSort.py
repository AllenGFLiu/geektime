#   基于Python实现冒泡排序-BubbleSort
#   Author: AllenGFLiu
#   冒泡排序原理：
#   取list中的第一个元素循环跟其他元素比对，如果前者大于后者，则二者交换位置，称为一次冒泡
#   如上冒泡动作执行 len(list) - 1 次即可
#   冒泡排序不需要额外空间，所以空间复杂度为 O(1)， 属于原地排序算法
#   在比较过程，只有>时才会交换位置，所以相同元素不会因为排序而换位，属于稳定排序算法


def bubbleSort(myList):
    length = len(myList)
    if length <= 1:
        return
    for i in range(length):
        exchange = False  # 当已经有序后，就不会发生元素交换了，就可以跳出循环，避免无效循环继续执行
        print(myList)  # 方便看每次排序之后的样子
        for j in range(length-i-1):
            if myList[j] > myList[j+1]:
                myList[j], myList[j+1] = myList[j+1], myList[j]
                exchange = True
        if not exchange:
            return
        

if __name__ == "__main__":
    List = [3, 5, 2, 1, 4]
    print('排序前:')
    print(List)
    bubbleSort(List)
    print('排序后:')
    print(List)