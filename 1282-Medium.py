## 1282. Group the People Given the Group Size They Belong To

## There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.
## You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if 
## groupSizes[1] = 3, then person 1 must be in a group of size 3.

## Return a list of groups such that each person i is in a group of size groupSizes[i].

def groupThePeople(groupSizes):
    result=[]
    groups={}
    for i, group in enumerate(groupSizes):
        if group not in groups:
            groups[group]=[i]
        else:
            groups[group].append(i)
        if len(groups[group])==group:
            result.append(groups[group])
            groups[group]=[]
    return result


if __name__=='__main__':
    groupSizes = [3,3,3,3,3,1,3]
    print(groupThePeople(groupSizes))