class Node:
    def __init__(self):
        self.childs = []  # List of children nodes
        self.value = None  # Character value of the node
        self.key = False   # Marks the end of a word


class Trie:
    def __init__(self):
        self.tree = Node()  # Root node of the Trie

    def insert(self, word: str) -> None:
        curr_node = self.tree
        for character in word:
            found = False
            # Check if the current character already exists in the current node's children
            for child in curr_node.childs:
                if child.value == character:
                    curr_node = child  # Move to the child node
                    found = True
                    break
            # If character not found, create a new node for the character
            if not found:
                new_node = Node()
                new_node.value = character
                curr_node.childs.append(new_node)
                curr_node = new_node
        curr_node.key = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        curr_node = self.tree
        for character in word:
            found = False
            # Traverse through the children to find the character
            for child in curr_node.childs:
                if child.value == character:
                    curr_node = child
                    found = True
                    break
            if not found:
                return False
        return curr_node.key  # Return True if it's the end of the word

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.tree
        for character in prefix:
            found = False
            for child in curr_node.childs:
                if child.value == character:
                    curr_node = child
                    found = True
                    break
            if not found:
                return False
        return True

    def __str__(self):
        result = []
        self._collect_words(self.tree, "", result)
        return "\n".join(result)

    def _collect_words(self, node, prefix, result):
        if node.key:
            result.append(prefix)
        for child in node.childs:
            self._collect_words(child, prefix + child.value, result)