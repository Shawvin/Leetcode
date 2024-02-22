## 201. Bitwise AND of Numbers Range

## Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

def rangeBitwiseAnd(left,right):
    result=0
    if left==0 or right==0:
        return result
    if left==right:
        return left
    left_i=[]
    right_i=[]
    idx=0
    while left or right:
        if left & 1:
            left_i.append(idx)
        if right & 1:
            right_i.append(idx)
        left>>=1
        right>>=1
        idx+=1
    left_i=left_i[::-1]
    right_i=right_i[::-1]
    n=min(len(left_i),len(right_i))
    for i in range(n):
        if left_i[i]!=right_i[i]:
            return result
        else:
            result+=2**left_i[i]
    return result

def rangeBitwiseAnd2(left,right):
    result=0
    while left!=right:
        left>>=1
        right>>=1
        result+=1
    return left<<result

def rangeBitwiseAnd3(left,right):
    while right>left:
        right &=(right-1)
    return right

if __name__=='__main__':
    left = 5
    right = 7
    print(rangeBitwiseAnd3(left,right))