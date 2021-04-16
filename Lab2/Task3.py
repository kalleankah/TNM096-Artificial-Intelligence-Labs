from time import time
from aima.csp import CSP

#Variable list
timeandplace = []
classrooms = ["TP51", "SP34", "K3"]
timeslots = [9,10,11,12,1,2,3,4]

classes = ["MT101","MT102","MT103","MT104","MT105","MT106","MT107","MT201","MT202","MT203","MT204","MT205","MT206","MT301","MT302","MT303","MT304","MT401","MT402","MT403","MT501","MT502"]

for time in timeslots:
    for classroom in classrooms:
        timeandplace.append(classroom + "-" + str(time))
    
#Define problem as class schedule 
def schedule_constraints(A,a,B,b):
    defiesConstraint = False
    if A == B:
    return defiesConstraint
    
class schedule(CSP):
    def __init__(self, n):
        """Initialize data structures for n Queens."""
        CSP.__init__(self, list(range(n)), UniversalDict(list(range(n))),
                     UniversalDict(list(range(n))), queen_constraint)

        self.rows = [0]*n
        self.ups = [0]*(2*n - 1)
        self.downs = [0]*(2*n - 1)

    def __init__(self, timeandplace, UniversalDict(classes), UniversalDict(neighbors), schedule_constraints):
