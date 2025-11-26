class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []


class Solution:
    def insert(self, root, word):
        node = root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            if len(node.suggestions) < 3:
                node.suggestions.append(word)
                
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        root = TrieNode()
        for w in products:
            self.insert(root, w)

        # Build answer
        ans = []
        node = root

        for c in searchWord:
            if c in node.children:
                node = node.children[c]
                ans.append(node.suggestions)
            else:
                # no matches from here onward
                ans.extend([[]] * (len(searchWord) - len(ans)))
                break

        return ans
        