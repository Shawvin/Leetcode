## 150. Evaluate Reverse Polish Notation

def evalRPN(tokens):
    st=[]
    cur=None
    while len(tokens)>0:
        cur=tokens.pop()
        if cur in '+-*/':
            st.append(cur)
        elif len(st)==0:
            return int(cur)
        elif st[-1] in '+-*/':
            st.append(cur)
        else:
            cur1=st.pop()
            sign=st.pop()
            if sign=='+':
                res=int(cur)+int(cur1)
            elif sign=='-':
                res=int(cur)-int(cur1)
            elif sign=='*':
                res=int(cur)*int(cur1)
            elif sign=='/':
                res=int(int(cur)/int(cur1))
            tokens.append(str(res))

def evalRPN2(tokens):
    st=[]
    for token in tokens:
        if token in '+-*/':
            num2=st.pop()
            num1=st.pop()
            if token=='+':
                st.append(num1+num2)
            elif token=='-':
                st.append(num1-num2)
            elif token=='*':
                st.append(num1*num2)
            elif token=='/':
                st.append(int(num1/num2))
        else:
            st.append(int(token))
    return st.pop()


if __name__=='__main__':
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evalRPN(tokens))