## 2483. Minimum Penalty for a Shop


def bestClosingTime(scustomers):
    penalty=[0]*(len(customers)+1)
    count=0
    for customer in customers:
        if customer=='Y':
            count+=1
    penalty[0]=count
    penalty[-1]=len(customers)-count
    min_penalty=penalty[0]
    hour=0
    for i in range(1, len(customers)):
        if customers[i-1]=='Y':
            penalty[i]=penalty[i-1]-1
        if customers[i-1]=='N':
            penalty[i]=penalty[i-1]+1
        if min_penalty>penalty[i]:
            min_penalty=penalty[i]
            hour=i
    if min_penalty>penalty[-1]:
        min_penalty=penalty[-1]
        hour=len(customers)
    return hour

if __name__=='__main__':
    customers = "YYNY"
    print(bestClosingTime(customers))