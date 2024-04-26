## 207. Course Schedule

from collections import defaultdict

def canFinish(numCourses, prerequisites):
    graph=defaultdict(list)
    for a,b in prerequisites:
        graph[a].append(b)
    q=[]
    for i in range(numCourses):
        q.append(i)
        taken=set()
        taken.add(i)
        while q:
            cur=q.pop()
            for pre in graph[cur]:
                if pre not in taken:
                    taken.add(pre)
                    q.append(pre)
                if pre==i:
                    return False
    return True

if __name__=='__main__':
    numCourses = 4
    prerequisites = [[0,1],[3,1],[1,3],[3,2]]
    print(canFinish(numCourses, prerequisites))