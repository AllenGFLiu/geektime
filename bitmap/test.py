class BitMap:
    def __init__(self, bit_nums):
        self._b_nums = bit_nums
        self._bytes = bytearray(bit_nums//8+1)

    def set_bit(self, k):
        if k > self._b_nums or k < 1:
            return False

        self._bytes[k//8] |= (1 << k%8)
        return True

    def get_bit(self, k):
        if k > self._b_nums or k < 1:
            return False
        
        return self._bytes[k//8] & (1<< k%8) != 0