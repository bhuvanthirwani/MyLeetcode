class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        D={}
        for word in words:
            if word in D:
                D[word] += 1
            else:
                D[word] = 1
        ans = []
        for i in D:
            ans.append((D[i], i))
        ans = sorted(ans, key=lambda x: (-x[0], x[1]))
        top_k=[]
        for i in range(k):
            top_k.append(ans[i][1])
        return top_k
