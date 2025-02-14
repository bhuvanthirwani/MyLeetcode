class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        from collections import deque
        queue = deque([""])
        Map={
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"]
        }
        ans = []
        count = 0
        for digit in digits:
            length = len(queue)
            while(length):
                ele = queue.popleft()
                for letter in Map[digit]:
                    queue.append(ele+letter)
                length -= 1
            count += 1
            if count == len(digits):
                return list(queue)
        return []