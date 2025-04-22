class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        right = []
        maxl, maxr=0,0
        for i in height:
            left.append(maxl)
            maxl=max(maxl, i)
        for i in range(len(height)-1, -1, -1):
            right.append(maxr)
            maxr=max(maxr, height[i])
        right=right[::-1]
        s=0
        # print(left, right, height)
        j=0
        while j<len(height):
            # print("KKK: ", j)
            if j==0 or j==len(height)-1:
                j+=1
                continue
            else:
                # print("j: ", j, min(left[j], right[j]))
                if min(left[j], right[j]) >= height[j]:
                    s+= min(left[j], right[j]) - height[j]
                # print("Hello: ",j, s, j)
            j +=1
            # print("j: ", j)
        return s