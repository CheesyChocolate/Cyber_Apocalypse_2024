from z3 import *

# Create a solver instance
solver = Solver()

# Define variables
var = [Int(f"var_{i}") for i in range(22)]

# Add constraints for variables to be within the range 0 to 255
for i in range(22):
    solver.add(And(var[i] >= 30, var[i] <= 160))

# Add constraints
solver.add(var[7] - var[18] == var[8] - var[9])
solver.add(var[6] + var[10] == var[16] + var[20] + 12)
solver.add(var[8] * var[14] == var[13] * var[18] * 2)
solver.add(var[19] == var[6])
solver.add(var[9] + 1 == var[17] - 1)
solver.add(var[11] / (var[5] + 7) == 2)
solver.add(var[5] + var[2] / 2 == var[1])
solver.add(var[16] - 9 == var[13] + 4)
solver.add(var[12] / 3 == 17)
solver.add((var[4] - var[5]) + var[12] == var[14] + 20)
solver.add((var[12] * var[15]) / var[14] == 24)
solver.add(var[18] == 173 - var[4])
solver.add(var[6] == 63 + var[5])
solver.add(32 * var[16] == var[7] * var[0])
solver.add(125 == var[21])
solver.add(var[3] - var[2] == 57)
solver.add(var[17] - var[15] == var[18] + 1)

# Add self-defined constraints to define 'HTB{' and '}' characters
solver.add(var[0] == 72)
solver.add(var[1] == 84)
solver.add(var[2] == 66)
solver.add(var[3] == 123)
solver.add(var[21] == 125)

# add other self-defined constraints to prevent the solver from finding other solutions
solver.add(var[4] != 123)   # '{'
solver.add(var[10] != 40)   # '('
solver.add(var[20] != 32)   # ' '
solver.add(var[20] != 30)   # '\x1e'
solver.add(var[20] != 31)   # '\x1f'
# solver.add(var[10] != 39) # '\''
# solver.add(var[10] != 37) # '%'
# solver.add(var[10] != 36) # '$'
# solver.add(var[20] == 33) # '!'

# Check if the constraints are satisfiable
if solver.check() == sat:
    # Get the model
    model = solver.model()

    # Extract values
    flag = []
    for i in range(22):
        flag.append(model[var[i]].as_long())
    print("Flag:", flag)

    # to convert list of integers to string
    new_flag = ''.join(list(map(lambda z:chr(z), list(flag))))
    print("Flag:", new_flag)
else:
    print("Constraints are unsatisfiable.")
