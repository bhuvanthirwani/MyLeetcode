class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        D={}
        count = 0
        for i in range(len(nums)):
            flag = False
            if k-nums[i] in D:
                if D[k-nums[i]] >= 1:
                    # print("Hurrah: ", i)
                    count += 1
                    D[k-nums[i]] -= 1
                    flag = True
                    if D[k-nums[i]] == 0:
                        del D[k-nums[i]]
                        
                        # print("Deleted: ", k-nums[i], D)
                
            if nums[i] not in D and flag == False:
                D[nums[i]] = 1
                # print("Added: ", nums[i])
            else:
                if nums[i] in D:
                    D[nums[i]] += 1
            
            # print("i: ",i ,nums[i], D)
        return count
            