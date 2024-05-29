## 1404. Number of Steps to Reduce a Number in Binary Representation to One

def numSteps(s):
    incre=False
    count=0
    for i in range(len(s))[::-1]:
        if not incre and s[i]=='0':
            count+=1
        elif incre and s[i]=='0':
            count+=2
            incre=True
        elif not incre and s[i]=='1':
            if i!=0:
                count+=2
                incre=True
        else:
            count+=1
            incre=True
    return count

if __name__=='__main__':
    s = "11000"
    print(numSteps(s))