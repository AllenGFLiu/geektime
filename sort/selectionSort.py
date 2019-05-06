#   基于Python实现选择排序
#   Author: AllenGFLiu
#   选择排序实现原理：
#   跟插入排序有相似的地方，也是把原始list看成两部分
#   首先对原始list循环比对，找出最小值
#   然后让最小值与原始list的第一位互换位置,如此循环
#   基于如上的原理，可知选择排序是原地算法，但不是稳定算法，并且时间复杂度是O(n^2),很少使用此算法，作为开拓眼界即可

def insertionSort(myList):
    length = len(myList)
    if length <= 1:
        return

    for i in range(length):
        minIndex = i
        for j in range(i+1, length):
            if myList[minIndex] > myList[j]:
                minIndex = j
        myList[i], myList[minIndex] = myList[minIndex], myList[i]


if __name__ == "__main__":
    List = [3, 5, 2, 1, 4]
    print('排序前:')
    print(List)
    insertionSort(List)
    print('排序后:')
    print(List)