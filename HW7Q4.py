# import numpy as np

# P = np.array([[0.97,0.03,0,0], [0,0,0.9,0.1], [0.97,0.03,0,0], [0,0,0.9,0.1]])

# # Calculates the eigenvalues of P and a left eigenvector
# # for each eigenvalue.
# # We need to transpose P to find the left eigenvectors. Can
# # also use P.T to transpose P.
# u,v = np.linalg.eig(np.transpose(P))

# # Prints eigenvalues, then eigenvectors. The *columns* of v
# # are the eignevectors.
# print(u)
# print(v)

# # To get an eigenvector which is a probability distribution,
# # you will need to multiply by 1/sum(v) so the sum of
# # coordinates is 1.




##### Alternate code using SciPy. #####

import numpy as np
import scipy as sp

P = np.array([[0.97, 0.03, 0, 0], [0, 0, 0.9, 0.1], [0.97, 0.03, 0, 0], [0, 0, 0.9, 0.1]])

# Instead of transposing P, write left=True and right=False.
u,v = sp.linalg.eig(P, left=True, right=False)
v = v* (1/np.sum(v))  # Normalize the eigenvector to be a probability distribution.

# The output may include "j". j is the imaginary unit sqrt(-1).
print(u)
print(v)
