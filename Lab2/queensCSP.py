"""  TASK2/LAB2    TNM096   
     Run the various CSP solvers on the nQueens problem            """

from time import time
from datetime import timedelta
from aima.csp import backtracking_search, NQueensCSP, min_conflicts, mrv, \
    forward_checking, AC3


def secondsToStr(t):
    return str(timedelta(seconds=t))

def now():
    return secondsToStr(time())
    

# 1. Set up the problem and starting time
n = 5

print("\nStarting at at  "+now()[12:20])
print("problem with n =",n)
start = time()

problem = NQueensCSP(n)

# 2. Solve the problem
solution = backtracking_search(problem)
#solution = AC3(problem); 
#solution = min_conflicts(problem)


# 3. Print the results

# Handle AC3 solutions (boolean values) first, they behave differently.
if type(solution) is bool:
    if solution and problem.goal_test(problem.infer_assignment()):
        print("AC3 Solution:")
        print(problem.curr_domains)
    else:
        print("AC3 Failure")
        print(problem.curr_domains)
# Handle other solutions next
elif problem.goal_test(solution):
    print("Solution:", solution)
else:
    print("Failed - domains: " + str(problem.curr_domains))
    #problem.display(problem.infer_assignment())


# 4. Print elapsed time

end = time()
elapsed = end-start
print("\nElapsed time ",  secondsToStr(elapsed)[0:15])