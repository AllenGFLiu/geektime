# 二分查找樹特性:
# 首先,這是一個樹,並且是一個二叉樹,所以需要定義樹中節點是按照TreeNode格式
# 之後,二分查找樹要求:樹中任意一個節點,其左子樹的節點值都小於本節點,而其右子樹的節點值都大於等於本節點
#
# 按照如上特性,極度不平衡的二叉查找樹會退化成單鏈表
# 另外,按照中序遍歷二分查找樹,能得到有序的數組
#
# Author: AllenGFLiu
# #####################################################


class TreeNode:
    """二叉樹中每個節點都有三個屬性

    _val : 存儲節點值

    left : 指向左子節點的指針

    right : 指向右子節點的指針
    """
    def __init__(self, value):
        self._val = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """實現二分查找樹的初始化/插入/查找/刪除

    __init__ : 初始化一個空的二叉查找樹

    insert : 向二叉查找樹中插入一個值為value的節點.
    若樹是空的,則直接給樹的根節點賦值為新節點;
    若樹中已經有值,按照二叉查找樹的特性(左小右大),定位到某葉子節點,
    為該葉子節點插入一個左或者右子節點.

    find : 查找二叉查找樹中是否有節點值(node._val)等於查找值value的節點,
    若有,按照二叉查找樹的特性(左小右大),定位到某葉子節點,返回該節點;
    若無,返回None.

    delete : 查找并定位到某個值等於value的節點,根據以下情形執行對應的刪除動作:
    情形一: 要刪除的節點有兩個子節點,此時需要找到該節點右子樹中最小的值節點,替換到原來的節點上,
    并把此最小值節點從原來的位置刪除;
    情形二和情形三: 要刪除的節點是葉子節點或者只有一個子節點,那麼定位到以後執行刪除動作即可.
    綜上兩大種情形,我們都是要先定位的,所以delete代碼中對兩個子節點的情形做一個專門的定位,
    剩下的動作,就可以用一直的代碼了
    """
    def __init__(self, value):
        self._root = None

    def insert(self, value):
        # 若為空樹
        if self._root is None:
            self._root = TreeNode(value)
            return

        # 若已經有值
        # 定位
        parent = None
        node = self._root
        while node:
            parent = node
            node = node.left if node._val > value else node.right

        # 新增子節點
        new_node = TreeNode(value)
        if parent._val > value:
            parent.left = new_node
        else:
            parent.right = new_node

    def find(self, value):
        node = self._root
        # 定位
        while node and node._val != value:
            node = node.left if node._val > value else node.right
        return node

    def delete(self, value):
        # 無論如何都是要先定位到要刪除的節點處的
        node = self._root
        parent = None
        while node and node._val != value:
            parent = node
            node = node.left if node._val > value else node.right

        # 空樹
        if node is None:
            return
        

        # 對於要刪除的節點有兩個子節點來說,要找到其右子樹中最小值的那個葉子節點,并替換要刪除的節點
        if node.left and node.right:
            right_smallest_parent = node
            right_smallest_node = node.right
            while right_smallest_node.left:
                right_smallest_parent = right_smallest_node
                right_smallest_node = right_smallest_node.left
            node._val = right_smallest_node._val
            parent, node = right_smallest_parent, right_smallest_node

        # 如下的代碼是公用的
        # 如果要刪除的節點有兩個子節點,那上面的if 塊內的代碼就會執行,並且也發生了置換,但還剩下刪除最小值節點這一步
        # 如果要刪除的節點是葉子節點或者只有一個子節點,那上面的if 塊不會執行,就直接來次刪除來了
        # 所以if 塊內的parent和node 二次賦值這個動作很重要
        child = node.left if nodel.left else node.right
        if parent is None:
            # 這種情況比較特殊,是樹中只有兩個節點:根節點和它的一個子節點(左或右),並且根節點的值等於value
            self._root = child
        elif parent.left == node:
            parent.left = child
        else:
            parent.right = child






