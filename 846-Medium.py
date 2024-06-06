## 846. Hand of Straights

def isNStraightHand(hand, groupSize):
    num_dict={}
    for num in hand:
        num_dict[num]=num_dict.get(num,0)+1
    nums=sorted(list(num_dict.keys()))
    for num in nums:
        if num_dict[num]==0:
            continue
        elif num_dict[num]<0:
            return False
        else:
            base=num_dict[num]
            for i in range(groupSize):
                if num+i not in num_dict:
                    return False
                num_dict[num+i]-=base
    return True

if __name__=='__main__':
    hand = [1,2,3,6,2,3,4,7,8]
    groupSize = 3
    print(isNStraightHand(hand, groupSize))