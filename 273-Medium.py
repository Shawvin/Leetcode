## 273. Integer to English Words

def numberToWords(num):
    if num==0:
        return 'Zero'
    map=[None,'One', 'Two', 'Three', 'Four', 'Five',
    'Six', 'Seven', 'Eight', 'Nine','Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
    'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    val=[None, None, 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    res=[]
    while num>0:
        r=num%1000
        num=num//1000
        i=2
        curStr=[]
        while r>0:
            digit=r//(10**i)
            r=r%(10**i)
            if i==2:
                if digit>0:
                    curStr.append(map[digit])
                    curStr.append('Hundred')
            elif i==1:
                if digit>1:
                    curStr.append(val[digit])
                    if r!=0:
                        curStr.append(map[r])
                elif digit==1:
                    curStr.append(map[10+r])
                    break
                elif digit==0:
                    curStr.append(map[r])
            i-=1
        res.append(' '.join(curStr))
    for i in range(len(res)):
        if i==1 and res[i]!='':
            res[i]+=' Thousand'
        elif i==2 and res[i]!='':
            res[i]+=' Million'
        elif i==3 and res[i]!='':
            res[i]+=' Billion'
    print(res)
    return ' '.join([x for x in res[::-1] if x!=''])

if __name__=='__main__':
    num = 1000000
    print(numberToWords(num))