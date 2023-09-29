## 880. Decoded String at Index

## You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:
 
##If the character read is a letter, that letter is written onto the tape.
##If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.

def decodeAtIndex(s, k):
    total=0
    count=0
    temp=""
    stack=[]
    for ch in s:
        if ch not in '0123456789':
            temp+=ch
            total+=1
        else:
            num=int(ch)
            stack.append((count,temp))
            total=total*num
            count=total
            temp=''
        if total>k:
            break
    stack.append((total-len(temp),temp))
    print(stack)
    while stack:
        count,temp=stack.pop()
        base=count+len(temp)
        k=k%base
        if k>count:
            return temp[k-count-1]
        if k==0 and len(temp)!=0:
            return temp[-1:]      
                                        
if __name__=='__main__':
    s='a23'
    k=6
    print(decodeAtIndex(s, k))