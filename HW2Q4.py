from ortools.linear_solver import pywraplp


def main():
    # [START solver]
    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    # Create the variables.
    f1 = solver.NumVar(0, solver.infinity(), 'f1')
    f2 = solver.NumVar(0, solver.infinity(), 'f2')
    p = []
    for i in range(9, 15):
        p.append(solver.NumVar(0, solver.infinity(), 'p' + str(i)))

    print("Number of variables = ", solver.NumVariables())

    # Create the constraints.
    solver.Add(p[0] + p[1] + p[2] + p[3] + p[4] + p[5] <= 5)
    solver.Add(f1 + f2 + p[0] >= 4)
    solver.Add(f1 + f2 + p[0] + p[1] >= 3)
    solver.Add(f1 + f2 + p[0] + p[1] + p[2] >= 4)
    solver.Add(f1 + p[1] + p[2] + p[3] >= 6)
    solver.Add(f2 + p[2] + p[3] + p[4] >= 5)
    solver.Add(f1 + f2 + p[3] + p[4] + p[5] >= 6)
    solver.Add(f1 + f2 + p[4] + p[5] >= 8)
    solver.Add(f1 + f2 + p[5] >= 8)
    solver.Add(p[0] >= 0)
    solver.Add(p[1] >= 0)
    solver.Add(p[2] >= 0)
    solver.Add(p[3] >= 0)
    solver.Add(p[4] >= 0)
    solver.Add(p[5] >= 0)
    solver.Add(f1 >= 0)
    solver.Add(f2 == 3)
    print("Number of constraints = ", solver.NumConstraints())

    # Create the objective function.
    solver.Minimize(64*(f1 + f2) + 15*(p[0] + p[1] + p[2] + p[3] + p[4] + p[5]))
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print("Solution:")
        print("Objective value = ", solver.Objective().Value())
        print("f1 = ", f1.solution_value())
        print("f2 = ", f2.solution_value())
        print("p9 = ", p[0].solution_value())
        print("p10 = ", p[1].solution_value())
        print("p11 = ", p[2].solution_value())
        print("p12 = ", p[3].solution_value())
        print("p13 = ", p[4].solution_value())
        print("p14 = ", p[5].solution_value())
    else:
        print("The problem does not have an optimal solution.")
    
if __name__ == '__main__':
    main()