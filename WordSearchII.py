class TrieNode:
    def __init__(self):
        self.childs = {}
        self.isWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if child is None:
                child = TrieNode()
                node.childs[letter] = child
            node = child
        node.isWord = True
    
    def search(self, word):
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if child is None:
                return False
            node = child
        return node.isWord
    
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res
        
    def dfs(self, board, node, row, col, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        
        if row < 0 or row > len(board) - 1 or col < 0 or col > len(board[0]) - 1:
            return 
        
        tmp = board[row][col]
        node = node.childs.get(tmp)
        if not node:
            return
        board[row][col] = '#'
        self.dfs(board, node, row+1, col, path+tmp, res)
        self.dfs(board, node, row-1, col, path+tmp, res)
        self.dfs(board, node, row, col+1, path+tmp, res)
        self.dfs(board, node, row, col-1, path+tmp, res)
        board[row][col] = tmp