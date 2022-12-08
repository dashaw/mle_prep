# --------
# implement-trie-prefix-tree
# --------
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    """
    so we want to create a tree 


    time complexity: O(W*L) W words, L average length
    space compelxity: O(W*L)
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return True        

# ---------
# design-add-and-search-words-data-structure
# ---------
class TrieNode:

    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.search_hash = {}
        self.search_hash_add_update = False


    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children.keys():
                curr.children[c] = TrieNode()

            curr = curr.children[c]
        
        curr.end_of_word = True

        self.search_hash = {}

    def search(self, word: str) -> bool:
        
        if word in self.search_hash.keys():
            return self.search_hash[word]

        def dfs(node, char_q):
            if len(char_q) == 0:
                if node.end_of_word:
                    self.found = True
                    return True
                else:
                    return False
            
            elif char_q[0] == '.':
                for i in node.children.keys():
                    dfs(node.children[i], char_q[1:])
                    
            elif char_q[0] in node.children.keys():
                dfs(node.children[char_q[0]], char_q[1:])
                
            else:
                return False

        curr = self.root
        word_q = list(word)
        node_q = []
        node_q.append(curr)
        self.found = False

        dfs(curr, word_q)
        self.search_hash[word] = self.found
        return self.found
