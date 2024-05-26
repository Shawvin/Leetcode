## 551. Student Attendance Record I

def checkRecord(s):
    record=[0,0]
    for ch in s:
        if ch=='A':
            record[0]+=1
            record[1]=0
            if record[0]>1:
                return False
        elif ch=='L':
            record[1]+=1
            if record[1]>=3:
                return False
        else:
            record[1]=0
    return True

if __name__=='__main__':
    s = "PPALLP"
    print(checkRecord(s))