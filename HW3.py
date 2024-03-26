from ortools.linear_solver import pywraplp


def main():
    costs = [[6.21, 0.37, 4.69, 8.1, 8.93, 6.35, 4.38, 1.46],
             [1.02, 1.57, 2.06, 8.35, 7.02, 0.15, 8.39, 9.1],
             [8.31, 3.88, 8.22, 4.31, 2.1, 4.54, 9.46, 9.11],
             [2.34, 4.59, 7.24, 7.33, 7.36, 9.16, 7.4, 0.03],
             [7.25, 7.26, 5.25, 9.51, 9.48, 9.79, 2.85, 0.25],
             [6.03, 5.01, 1.02, 8.56, 4.09, 6.8, 0.82, 5.31],
             [9.38, 5.37, 3.82, 2.25, 4.49, 2.79, 5.9, 3.75],
             [0.35, 7.42, 6.47, 6.54, 4.92, 2.72, 0.67, 9.76]]
    n = 8
    roads = min_cost_village(n, costs)
    for road in roads:
        print(road[0], '--', road[1])


def min_cost_village(n, costs):
    # [START solver]
    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    # [END solver]

    # [START variables]
    # Create the variables.
    v = {}
    for i in range(n):
        for j in range(n):
            v[i, j] = solver.NumVar(0, 1, 'v' + str(i) + str(j))
    # [END variables]
    print("Number of variables =", solver.NumVariables())

    # Create the constraints.
    for i in range(n):
        solver.Add(solver.Sum([v[i, j] for j in range(n)]) == 1)

    for j in range(n):
        solver.Add(solver.Sum([v[i, j] for i in range(n)]) == 1)      

    # Create the objective function.
    objective = solver.Objective()
    for i in range(n):
        for j in range(n):
            objective.SetCoefficient(v[i, j], costs[i][j])
    objective.SetMinimization()
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print("Solution:")
        roads = []
        for i in range(n):
            for j in range(n):
                if v[i, j].solution_value() == 1:
                    roads.append((i, j))
        print("Objective value = ", solver.Objective().Value())
        return roads
    else:
        return None


if __name__ == '__main__':
    main()