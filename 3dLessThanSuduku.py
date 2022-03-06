from z3 import *
import math
import ast

# the size of the board
num_input = input("Please enter the size of the 3D sudoku:\n")
# convert string to integer
num = int(num_input)

# checks that the size of the board is greater than 2
if(num < 2):
    raise Exception(
        "\nThe size of the sudoku board must be greater than 2. Try again. \n")

# the matrix instance
instance_input = input(
    "Please enter the initial board instance you would like to solve! Remember, fill in 0 for empty intial cells\n")
instance = ast.literal_eval(instance_input)


# the list of constraints for the matrix instance of 3D logic sudoku
constraint_input = input(
    "\n\nPlease enter the list of constraints or enter to skip.\n\n - Constraint Symbols: '>', '<', '^2', '^3', 'n', and 'nn'\n\n - Coordinate Format: x_y_z (zero indexed)\n\n - Constraint format: (('symbol', (coordinate1), (coordinate2)), ... , ('symbol', (coordinate1), (coordinate2)))\n\nEnter Here:\n")
# starts with no constraints, user can skip and have no constraints listed
constraints = ()
# if the user inputs constraints, converts string to tuple
if constraint_input != "":
    constraints = ast.literal_eval(constraint_input)

# num x num x num matrix of integer variables
X = [[[Int("%s_%s_%s" % (i, j, k)) for k in range(num)]
      for j in range(num)]
     for i in range(num)]

# if confused on location of coordinates, uncomment these lines and run:
# print("Coordinates:\n")
# print(X)


# each cell contains a value in {1, ..., num}
cells_c = [And(1 <= X[i][j][k], X[i][j][k] <= num)
           for i in range(num) for j in range(num) for k in range(num)]

# each row contains a digit at most once
rows_c = []
for k in range(num):
    for j in range(num):
        temp = []
        for i in range(num):
            temp.append(X[i][j][k])
        rows_c.append(Distinct(temp[:]))

# each column contains a digit at most once
cols_c = []
for i in range(num):
    for k in range(num):
        temp = []
        for j in range(num):
            temp.append(X[i][j][k])
        cols_c.append(Distinct(temp[:]))

# each depth contains a digit at most once
depth_c = []
for j in range(num):
    for i in range(num):
        temp = []
        for k in range(num):
            temp.append(X[i][j][k])
        depth_c.append(Distinct(temp[:]))

sudoku_c = cells_c + rows_c + cols_c + depth_c

# sudoku instance, we use '0' for empty cells
instance_c = []
for k in range(num):
    for j in range(num):
        for i in range(num):
            if(instance[i][j][k] != 0):
                # if the instance is not an empty cell, the solver should add this value in
                instance_c.append(X[i][j][k] == instance[i][j][k])


# are the logic constraints correct?
# This variable changes to false if a constraint is not acceptable
logic_work = True

# constraints on values
# list of constraints on the instance
# constaints are listed in order of symbol, then the two coordinates
# that the symbol relation is in between
# the general format: ('symbol', (coordinate 1), (coordinate 2))
# where coordinate 1 and coordinate 2 follow (i, j, k)
# types of constraints are '>' '<' '^2' '^3' 'n' and 'nn'
instance_constraint = []
# goes through the list of constraints
for (constraint, (row1, column1, depth1), (row2, column2, depth2)) in constraints:
    # throws an error for an illegal coordinate for the instance
    if((row1 > (num - 1)) or (column1 > (num - 1)) or (depth1 > (num - 1)) or (row1 < 0) or (column1 < 0) or
       (depth1 < 0) or (row2 > (num - 1)) or (column2 > (num - 1)) or (depth2 > (num - 1)) or (row2 < 0) or
       (column2 < 0) or (depth2 < 0)):
        logic_work = False
        raise Exception(
            "\nThe first set of coordinates goes out of bounds. \nThe coordinates are in bounds from 0 to " + str(num - 1))
    # throws an error for an illegal type of logic constraint
    if((constraint != '<') and (constraint != '>') and (constraint != '^2') and (constraint != '^3') and (constraint != 'nn') and (constraint != 'n')):
        logic_work = False
        raise Exception(
            "\nOne of the logic symbol is not accepted. \nThe accepted logic constraints are: >, <, ^2, ^3, n, nn. Try again\n")
    # the second coordinate is greater than the first coordinate
    if(constraint == '<'):
        instance_constraint.append(
            X[row1][column1][depth1] < X[row2][column2][depth2])
    # the second coordinate is less than the first coordinate
    if(constraint == '>'):
        instance_constraint.append(
            X[row1][column1][depth1] > X[row2][column2][depth2])
    # the second coordinate is equal to the first coordinate squared
    if(constraint == '^2'):
        instance_constraint.append(X[row2][column2][depth2] == (
            (X[row1][column1][depth1]) * (X[row1][column1][depth1])))
    # the second coordinate is equal to the first coordinate cubed
    if(constraint == '^3'):
        instance_constraint.append(X[row2][column2][depth2] == (
            (X[row1][column1][depth1]) * (X[row1][column1][depth1]) * (X[row1][column1][depth1])))
    # the second coordinate value is a neighbor, either + 1 or - 1, of the first coordinate
    if(constraint == 'n'):
        # if coordinate is num, neighbor must be 1 or num -1
        # deals with "wrapping" the values of the board to each other
        if((instance[row1][column1][depth1]) == num):
            instance_constraint.append(Or((X[row2][column2][depth2] ==
                                           1), (X[row2][column2][depth2] == (X[row1][column1][depth1]) - 1)))
        # if coordinate is 1, neighbor must be 2 or num
        # deals with "wrapping" the values of the board to each other
        if((instance[row1][column1][depth1]) == 1):
            instance_constraint.append(Or((X[row2][column2][depth2] ==
                                           num), (X[row2][column2][depth2] == (X[row1][column1][depth1]) + 1)))
        # coordinates are + 1 or - 1 from each other
        else:
            instance_constraint.append(Or((X[row2][column2][depth2] == (
                X[row1][column1][depth1]) + 1), (X[row2][column2][depth2] == (X[row1][column1][depth1]) - 1)))
    # the second coordinate value is a non- neighbor, neither + 1 or - 1, of the first coordinate
    if(constraint == 'nn'):
        # if coordinate is num, neighbor can not be 1 or num -1
        # deals with "wrapping" the values of the board to each other
        if((instance[row1][column1][depth1]) == num):
            instance_constraint.append(Or((X[row2][column2][depth2] !=
                                           1), (X[row2][column2][depth2] != (X[row1][column1][depth1]) - 1)))
        # if coordinate is 1, neighbor can not be 2 or num
        # deals with "wrapping" the values of the board to each other
        if((instance[row1][column1][depth1]) == 1):
            instance_constraint.append(Or((X[row2][column2][depth2] !=
                                           num), (X[row2][column2][depth2] != (X[row1][column1][depth1]) + 1)))
        # coordinates are not + 1 or - 1 from each other
        else:
            instance_constraint.append(Or((X[row2][column2][depth2] != (
                X[row1][column1][depth1]) + 1), (X[row2][column2][depth2] != (X[row1][column1][depth1]) - 1)))


# will only run the solver if the logic constraints are correct or empty
if(logic_work):
    # initialize solver
    s = Solver()
    # add the known constraints to the solver and the initial instance
    s.add(sudoku_c + instance_c + instance_constraint)
    # solve and print the instance
    if s.check() == sat:
        m = s.model()
        r = [[[m.evaluate(X[i][j][k]) for k in range(num)]
              for j in range(num)]
             for i in range(num)]
        print_matrix(r)
    # unable to solve the instance
    else:
        print("failed to solve")
