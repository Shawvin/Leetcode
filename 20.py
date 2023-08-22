## 20. Valid Parentheses
## Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

def isValid(s):
    char_dict={'(':1,'{':2,'[':3,')':-1,'}':-2,']':-3}
    char_stack=[]
    for char in s:
        if char_dict[char]>0:
            char_stack.append(char)
        else:
            if len(char_stack)>0:
                char_out=char_stack.pop()
                if char_dict[char_out]+char_dict[char]!=0:
                    return False
            else:
                return False
    return True

if __name__=='__main__':
    s="()[]{}"
    print(isValid(s))