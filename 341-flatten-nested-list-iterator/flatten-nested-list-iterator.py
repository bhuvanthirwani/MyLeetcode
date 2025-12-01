# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list=nestedList
        self.index = 0
        self.flattened_list = None
        self.flatten_list
    
    def flatten_list(self, _list: [NestedInteger]):
        ans = []
        # print("Hello")
        
        for i in _list:
            if i.isInteger():
                # print("Integer: ", i)
                ans.append(i.getInteger())
            else:
                # print("List: ", i)
                ans.extend(self.flatten_list(i.getList()))
        return ans
    def next(self) -> int:
        self.index += 1
        if self.flattened_list:
            return self.flattened_list[self.index-1]
        else:
            
            return self.flattened_list[self.index-1]
        
    def hasNext(self) -> bool:
        if self.flattened_list == None:
            self.flattened_list = self.flatten_list(self.list)
        return self.index != len(self.flattened_list)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())