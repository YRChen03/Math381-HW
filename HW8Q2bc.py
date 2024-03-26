import numpy as np
import math

def transition_matrix(N):
    P = np.zeros((2 * N + 1, 2 * N + 1))
    for i in range(2 * N + 1):
        for j in range(2 * N + 1):
            P[i, j] = (math.factorial(2 * N) / (math.factorial(j) * math.factorial(2 * N - j))) * \
                      ((i / (2 * N)) ** j) * ((1 - i / (2 * N)) ** (2 * N - j))
    return P

def find_Q(P):
    Q = P[1:-1, 1:-1]
    return Q

def find_R(P):
    R = P[1:-1, [0, -1]]
    return R

def find_inv_IminusQ(Q):
    N = np.linalg.inv(np.eye(len(Q)) - Q)
    return N

def find_B(Q, R):
    B = find_inv_IminusQ(Q).dot(R)
    return B

def find_absorption_probability(i, N, R):
    B = find_B(N, R)
    return B[i - 1, 1]

def main():
    # Given values
    N_list = [10, 50, 100, 200]  # Corrected value of N to 50 as per the problem statement
    initial_copies = 10
    for N in N_list:
        P = transition_matrix(N)
        Q = find_Q(P)
        R = find_R(P)
        absorption_probability = find_absorption_probability(initial_copies, Q, R)
        print('N =', N)
        print(absorption_probability)
    i_list = [5, 10, 15, 20]
    N = 200
    for i in i_list:
        P = transition_matrix(N)
        Q = find_Q(P)
        R = find_R(P)
        absorption_probability = find_absorption_probability(i, Q, R)
        print('i =', i)
        print(absorption_probability)
if __name__ == '__main__':
    main()
