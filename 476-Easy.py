## 476. Number Complement

def findComplement(num):
    cur=num
    count=0
    while cur>0:
        cur=cur>>1
        count+=1
    return num^((1<<(count))-1)

if __name__=='__main__':
    num = 5
    print(findComplement(num))