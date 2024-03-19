## 849. Maximize Distance to Closest Person

## You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).
## There is at least one empty seat, and at least one person sitting.
## Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
## Return that maximum distance to the closest person.

def maxDistToClosest(seats):
    idx=-1
    max_space=0
    for i in range(len(seats)):
        if seats[i]:
            if idx==-1:
                max_space=i
            else:
                max_space=max(max_space, (i-idx)//2)
            idx=i
    return max(max_space,(len(seats)-1-idx))

if __name__=='__main__':
    seats=[1,0,0,0,1,0,1]
    print(maxDistToClosest(seats))