class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        _set = set(wordList)
        from collections import deque
        queue = deque([(beginWord, 1)])
        while queue:
            ele, steps = queue.popleft()
            if ele == endWord:
                return steps
            for i in range(len(ele)):
                for j in range(26):
                    word = ele[:i] + chr(ord('a') + j) + ele[i+1:]
                    if word in _set:
                        queue.append((word, steps + 1))
                        _set.remove(word)
        return 0