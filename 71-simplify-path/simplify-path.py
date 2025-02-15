class Solution:
    def simplifyPath(self, path: str) -> str:
        my_str = ""
        prev = ''
        for i in range(len(path)):
            if path[i] == '/':
                if prev == '/':
                    continue
                prev = '/'
                my_str += path[i]
            else:
                my_str += path[i]
                prev = ""

        # print(my_str)
        stack = my_str.split('/')
        # print(stack)
        A=[]
        count = 0
        for i in range(len(stack)-1, -1, -1):
            if stack[i] == '' or stack[i] == '.':
                continue
            if stack[i] == '..':
                count += 1
                continue
            else:
                if count == 0:
                    A.append(stack[i])
                else:
                    count -= 1
                

        ans = ''
        # print(A)
        for i in A[::-1]:
            if i != '':
                ans+='/' + i
        
        
        return ans if ans else '/'