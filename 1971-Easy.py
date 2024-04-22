## 1971. Find if Path Exists in Graph

def validPath(n, edges,source,destination):
    graph={}
    for item in edges:
        if item[0] in graph:
            graph[item[0]].append(item[1])
        else:
            graph[item[0]]=[item[1]]
        if item[1] in graph:
            graph[item[1]].append(item[0])
        else:
            graph[item[1]]=[item[0]]
    print(graph)
    visit=[False]*n
    visit[source]=True
    st=[]
    st.append(source)
    while st:
        cur=st.pop()
        if cur==destination:
            return True
        for v in graph.get(cur,[]):
            if not visit[v]:
                visit[v]=True
                st.append(v)
    return False

if __name__=='__main__':
    n=10
    edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
    source = 5
    destination = 9
    print(validPath(n, edges,source,destination))