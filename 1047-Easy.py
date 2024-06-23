## 1047. Remove All Adjacent Duplicates In String

def removeDuplicates(s: str) -> str:
    stack=[]
    for ch in s:
        if len(stack)==0 or stack[-1]!=ch:
            stack.append(ch)
        elif stack[-1]==ch:
            stack.pop()
    return ''.join(stack)

if __name__=='__main__':
    s = "abbaca"
    print(removeDuplicates(s))