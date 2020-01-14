# 開篇問題:有 1 千萬個整數,整數的範圍在 1 到 1 億之間.如何快速查找某個整數是否在這 1 千萬個整數中呢?
# 位圖是一種存儲結構
# 通過使用一個二進制位中的0和1來表示true和false,從而達到節省存儲空間的目的
# 編程語言中提供的布爾類型一般都是一個字節,所以我們可以通過位運算,用其中的某個位表示某個數字
# 下面的測試代碼中把1和3做了set_bit動作,結果分別為二進制格式的和1001(第一個1,2^3的3;第二個1,2^1的1)
# 當測試2時返回false,是因為1001 & 10(十進制的2) 是=0的 ,而1001 & 1000(十進制的3) 是!= 0的

# 開篇問題可以用散列表實現,內存佔用大概為 40MB(int類型(4個字節)* 1千萬 )
# 位圖中保存的數據範圍不是很大,如果很大,空間消耗不降反增
# 1億 個二進制大概佔用 12MB( 1bit * 1億)
# 10億 個二進制會佔用 120MB

class BitMap:

    def __init__(self, num_bits):
        self._num_bits = num_bits

        # num_bits是打算建制的位圖的二進制個數
        # Python中bytearray創建的是字節,按照1個字節8個bit進行換算,並向上多1個字節即8個bit
        self._bytes = bytearray(num_bits//8 + 1)  # bytearray(int n)创建一个指定长度的以零值填充的实例,該實例類似數組,可以通過從0開始的下標訪問內部元素

    def set_bit(self, k):
        """k為建制好的二進制位圖的下標,不能超過設定的二進制個數或小於1
        k//8定位的是bytearray創建對象的下標
        1 << k%8 和 bytearray對象的元素值 取 或
        """
        if k > self._num_bits or k < 1:
            return
        
        self._bytes[k//8] |= (1<<k%8)  # %的优先级比 << 高

    def check_bit(self, k):
        """k為建制好的二進制位圖的下標,不能超過設定的二進制個數或小於1
        k//8定位的是bytearray創建對象的下標
        1 << k%8 和 bytearray對象的元素值 取 與
        """
        if k > self._num_bits or k < 1:
            return
        
        return self._bytes[k//8] & (1<<k%8) != 0

    
if __name__ == "__main__":
    bitmap = BitMap(10)
    bitmap.setbit(1)
    bitmap.setbit(3)
    bitmap.setbit(6)
    bitmap.setbit(7)
    bitmap.setbit(8)

    for i in range(1, 11):
        print(bitmap.getbit(i))