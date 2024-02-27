## 2092. Find All People With Secret

## You are given an integer n indicating there are n people numbered from 0 to n - 1. You are also given a 0-indexed 2D integer array meetings 
## where meetings[i] = [xi, yi, timei] indicates that person xi and person yi have a meeting at timei. A person may attend multiple meetings at the same time. 
## Finally, you are given an integer firstPerson.

def findAllPeople(n, meetings, firstPerson):
    person_secret_time={} # the person who knows the secrets and the time they first knew
    person_secret_time[0]=0
    meet_graph={} # key: the person, the other persons who meets this person and when they meet
    meet_graph[0]=[(firstPerson,0)]
    meet_graph[firstPerson]=[(0,0)]
    meetings=sorted(meetings, key=lambda x:x[2])
    for x,y,time in meetings:
        if x not in meet_graph:
            meet_graph[x]=[(y,time)]
        elif x in meet_graph:
            meet_graph[x].append((y,time))
        if y not in meet_graph:
            meet_graph[y]=[(x,time)]
        elif y in meet_graph:
            meet_graph[y].append((x,time))
    st=[]
    st.append((0,0))
    while st:
        p,time=st.pop(0)
        if p in person_secret_time and person_secret_time[p]>time:
            person_secret_time[p]=time
        for p2,time2 in meet_graph[p]:
            if p2 in person_secret_time and time2<person_secret_time[p2] and time2>=time:
                person_secret_time[p2]=time2
                st.append((p2,time2))
            if p2 not in person_secret_time and time2>=person_secret_time[p]:
                person_secret_time[p2]=time2        
                st.append((p2,time2))
    return sorted(list(person_secret_time.keys()))

if __name__=='__main__':
    n=5
    meetings=[[0,1,1],[1,4,2],[2,4,3],[0,4,4],[1,2,1]]
    firstPerson=3
    print(findAllPeople(n, meetings, firstPerson))