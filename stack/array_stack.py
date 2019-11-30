#-*- coding:utf-8 -*-
# 栈特性:
# 队列最大的特性就是先进后出，后进先出，最形象的比喻就是摞在一起的盘子
# 用数组可以实现栈，链表也可以实现栈
# 栈主要有两个动作：压栈push和出栈pop
#
# Author: AllenGFLiu
# #####################################################


class ArrayStack():
    """使用Python内部容器list来模拟数组，实现栈的数据结构。
    基于数组的栈，一般都有容量限制。
    
    push:压入栈，若是已满则返回False,压入成功则返回True.

    pop:出栈，正常出栈返回出栈的值，若无数据可出，则返回None.
    """
    def __init__(self, capacity):
        self.array = ['*']*capacity  # 对self.array初始化，只是为了方便展示结构体
        self.capacity = capacity
        self.count = 0

    def push(self, value):
        if self.count == self.capacity:
            return False

        self.array[self.count]=value
        self.count += 1
        return True
        
    def dynamic_push(self, value):
        if self.count == self.capacity:
            new_list = ['*'] * self.capacity
            self.capacity *= 2
            self.array.extend(new_list)

        self.array[self.count] = value
        self.count += 1
        return True

    def pop(self):
        if self.count == 0:
            return None

        pop_value = self.array[self.count-1]
        self.array[self.count-1]='*'
        self.count -= 1
        return pop_value

    def __repr__(self):
        return '|'.join(self.array)


if __name__ == '__main__':
    my_stack = ArrayStack(3)
    my_stack.push('a')
    my_stack.push('b')
    my_stack.push('c')
    my_stack.dynamic_push('d')
    print(my_stack)
    value = my_stack.pop()
    print(value)
    print(my_stack)
