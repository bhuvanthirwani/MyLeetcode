class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m=len(flowerbed)
        for i in range(m):
            if flowerbed[i] == 0:
                if i==0 and i+1 < m:
                    if flowerbed[i+1] == 0:
                        n-=1
                        flowerbed[i] = 1
                elif i==m-1 and i-1 >= 0:
                    if flowerbed[i-1] == 0:
                        n-=1
                        flowerbed[i] = 1
                elif m==1:
                    n-=1
                    flowerbed[i] = 1
                elif flowerbed[i+1]==0 and flowerbed[i-1]==0:
                    n-=1
                    flowerbed[i] = 1
        return n<=0