## 319. Bulb Switcher

## There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.
## On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, 
## you toggle every i bulb. For the nth round, you only toggle the last bulb.
## Return the number of bulbs that are on after n rounds.

def bulbSwitch(n):
    light={}
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j%i==0:
                light[j]=light.get(j,0)+1
    count=0
    for key in light:
        if light[key]%2==1:
            count+=1
    return count

def bulbSwitch2(n):
    count=0
    for i in range(1,n+1):
        if i*i<=n:
            count+=1
        else:
            break
    return count

if __name__=='__main__':
    n=9999
    print(bulbSwitch(n))