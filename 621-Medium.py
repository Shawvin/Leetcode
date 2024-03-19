## 621. Task Scheduler

## You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. 
## Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: 
## identical tasks must be separated by at least n intervals due to cooling time.
## 
## ​Return the minimum number of intervals required to complete all tasks.

def leastInterval(tasks, n):
    task_dict={}
    chunck=0
    for task in tasks:
        task_dict[task]=task_dict.get(task,0)+1
        chunck=max(chunck, task_dict[task])
    idle=(chunck-1)*n
    idle+=chunck-1
    for task in task_dict:
        idle-=min(chunck-1, task_dict[task])
    return len(tasks)+idle if idle>=0 else len(tasks)

if __name__=='__main__':
    tasks = ["A","A","A","B","B","B"]
    n=2
    print(leastInterval(tasks, n))