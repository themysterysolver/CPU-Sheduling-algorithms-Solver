import re

def algoSolver(at,bt,option,tq=None,p=None):
    at = list(map(int,re.split(r'\s+',at.strip())))
    bt = list(map(int,(re.split(r'\s+',bt.strip()))))
    if len(at)!=len(bt):
        return None
    if p:
        priority = list(map(int,(re.split(r'\s+',p.strip()))))
        if len(priority)!=len(at):
            return False

    # print(option)
    # print(tq,p)
    ans  = {}
    if option == "First come first served(FCFS)":
        ans = FCFS(at,bt)
    elif option == "Shortest job first(SJF)":
        ans = SJF(at,bt)
    elif option == "Shortest remaining time first(SRTF)":
        pass
    elif option == "Premptive Priority scheduling":
        pass
    elif option == "Non-Premptive priority scheduling":
        pass
    elif option == "Round robin(RR)":
        pass

    return ans

def FCFS(at,bt):
    n = len(at)
    ct = [0]*n
    tat = [0]*n
    wt = [0]*n

    process = sorted(range(n),key=lambda i:at[i])

    time = 0
    for i in process:
        if time<at[i]:
            time = at[i]
        time+=bt[i]
        ct[i] = time
        tat[i] = ct[i]-at[i]
        wt[i] = tat[i]-bt[i]

    return {"Process":[chr(ord('A')+i) for i in range(n)],"Arrival Time":at,"Burst Time":bt,"Completion Time":ct,"Turn Around Time":tat,"Waiting Time":wt}

def SJF(at,bt):
    n = len(at)
    ct = [0]*n
    tat = [0]*n
    wt = [0]*n
    
    completed = [False]*n
    done = 0
    time = 0

    process = sorted(range(n),key=lambda i:at[i])

    while done<n:
        idx = -1
        minbt = float('inf')
        for i in process:
            if not completed[i] and at[i]<=time:
                if bt[i]<minbt:
                    idx = i
                    minbt = bt[i]

        if idx==-1:
            time+=1
        else:
            time+=bt[idx]
            ct[idx] = time
            completed[idx] = True
            done+=1
            tat[idx] = ct[idx]-at[idx]
            wt[idx] = tat[idx]-bt[idx]


    return {"Process":[chr(ord('A')+i) for i in range(n)],"Arrival Time":at,"Burst Time":bt,"Completion Time":ct,"Turn Around Time":tat,"Waiting Time":wt}        
    
