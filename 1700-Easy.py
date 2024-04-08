## 1700. Number of Students Unable to Eat Lunch

def countStudents(students, sandwiches):
    s_dict={}
    for i in students:
        s_dict[i]=s_dict.get(i,0)+1
    sa_dict={}
    count=0
    for i in sandwiches:
        sa_dict[i]=sa_dict.get(i,0)+1
        count+=1
        if sa_dict[i]>s_dict.get(i,0):
            return len(sandwiches)-count+1
    return 0

def countStudents2(students, sandwiches):
    s_dict={}
    for i in students:
        s_dict[i]=s_dict.get(i,0)+1
    remain=len(sandwiches)
    for i in sandwiches:
        if s_dict.get(i,0)==0:
            break
        s_dict[i]-=1
        remain-=1
    return remain

if __name__=='__main__':
    students = [1,1,1,0,0,1]
    sandwiches = [1,0,0,0,1,1]
    print(countStudents2(students, sandwiches))