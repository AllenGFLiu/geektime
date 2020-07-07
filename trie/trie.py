# Trie树是为了解决字符串快速匹配问题的数据结构
# Trie树的本质是利用字符串之间的公共前缀，將重复的前缀合并在一起，从而实现快速查找。
# Trie树不适用于精确查找，精确查找适合用散列表或红黑树这种更高效的数据结构。

class TrieNode:
    def __init__(self, data):
        self._data = data
        self._children = [None]*26  # every trienode has a children array of 26 elements
        self._is_ending_char = False  # 表示是否为字符串最后的一个字符


class Trie:
    def __init__(self):
        self._root = TrieNode('/')

    def insert(self, string):
        node = self._root
        for index, char in map(lambda x: (ord(x)-ord('a'), x), string):
            if not node._children[index]:
                node._children[index] = TrieNode(char)  # split string into one char
                                                        # the second char saved in first char's children array; and so on
            node = node._children[index]  # node要替换成刚插入的char对应的node
        node._is_ending_char = True  # 此时node是最后一个字符，所以须设定为True

    def find(self, pattern):
        node =self._root
        for index in map(lambda x: ord(x)-ord('a'), pattern):
            if not node._children[index]: return False
            node = node._children[index]
        return node._is_ending_char

    def startswith(self, prefix):
        node = self._root
        for index in map(lambda c: ord(c)-ord('a'), prefix):
            if not node._children[index]: return False
            node = node._children[index]

        return True  # 不管是否匹配到最後一個字母,都返回TRUE


if __name__ == '__main__':
    strs = ['how', 'hi', 'her', 'hello', 'so', 'see']
    trie = Trie()
    for s in strs:
        trie.insert(s)

    for s in strs:
        print(trie.find(s))

    print(trie.find('he'))
    print(trie.startswith('he'))
        