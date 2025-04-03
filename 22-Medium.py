## 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

def generateParenthesis(n: int) -> list[str]:
    c=[n,n]
    res=[]
    def backtrack(c, res, cur):
        if c[0]>c[1]:
            return
        if c[1]==0:
            res.append(cur)
            return
        
        if c[0]>0:
            newcur=cur+'('
            c[0]-=1
            backtrack(c, res, newcur)
            c[0]+=1
        if c[1]>c[0]:
            newcur=cur+')'
            c[1]-=1
            backtrack(c, res, newcur)
            c[1]+=1
    
    backtrack(c, res, '')
    return res

if __name__=='__main__':
    n = 5
    print(generateParenthesis(n))