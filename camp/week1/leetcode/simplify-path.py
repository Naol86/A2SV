class Solution:
    def simplifyPath(self, path: str) -> str:
        lis = path.split('/')
        stack = []
        for dirc in lis:
            if dirc == '.':
                continue
            if dirc == '..':
                if stack:
                    stack.pop()
            elif len(dirc) != 0:
                stack.append(dirc)
        print(stack)
        return '/' + '/'.join(stack)