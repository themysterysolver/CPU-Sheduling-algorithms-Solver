import re

def algoSolver(at,bt,option,tq=None,p=None):
    at = re.split(r'\s+',at.strip())
    bt = re.split(r'\s+',bt.strip())
    if len(at)!=len(bt):
        return None
    if p:
        priority = re.split(r'\s+',p.strip())
        if len(priority)!=len(at):
            return False

    # print(option)
    # print(tq,p)
    if option == "First come first served(FCFS)":
        pass
    elif option == "Shortest job first(SJF)":
        pass
    elif option == "Shortest remaining time first(SRTF)":
        pass
    elif option == "Premptive Priority scheduling":
        pass
    elif option == "Non-Premptive priority scheduling":
        pass
    elif option == "Round robin(RR)":
        pass

    return True
    
    
