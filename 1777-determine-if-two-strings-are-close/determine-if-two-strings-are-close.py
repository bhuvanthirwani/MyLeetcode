class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        D1,D2={},{}
        n,m=len(word1),len(word2)
        if n!=m:
            return False
        for i in range(len(word1)):
            if word1[i] not in D1:
                D1[word1[i]]=0
            if word2[i] not in D2:
                D2[word2[i]]=0
            D1[word1[i]]+=1
            D2[word2[i]]+=1

        for l1 in D1:
            flag = 0
            for l2 in D2:
                if l1 not in D2 or l2 not in D1:
                    return False
                if D2[l2] != -1 and D2[l2] == D1[l1]:
                    D2[l2] = -1
                    flag=1
                    break
            if flag == 0:
                return False
        return True