This is a 3D "less than" sudoku with some additional constraints.

# SET UP INSTRUCTIONS

- Install python3 if not already on your computer: https://installpython3.com/mac/
- clone git repository
- cd to the repository directory
- run "pip install -r requirements.txt" to install necessary packages
  - replace "pip" as necessary for your python3 installation
- run the file!

# HOW TO RUN FILE:

the program takes three inputs: the size of the sudoku, the initial board which MUST MATCH the size input of the sudoku, and the constraints.

    - size is for the size of the sudoku board. One integer

    - instance is the matrix instance that you'd like to solve.

    - constraints are the list of constraints for the instance of the board

The board coordinates go from 0 to n - 1, where n is the size of the board.
to run file:

    - type in the command line: "python3 3dLessThanSudoku.py"

    - this prompt will follow: "Please enter the size of the 3D sudoku:"
        - enter the size you would like to run. For example, Please enter the size of the 3D sudoku: 4

    - Next, this promt will follow: "Please enter the initial board instance you would like to solve! Remember, fill in 0 for empty intial cells"

        - enter the initial board you would like to run. For example,
          (((0, 0, 0, 0),
          (0, 0, 0, 0),
          (0, 0, 0, 0),
          (0, 0, 0, 0)),

          ((0, 0, 0, 0),
          (0, 0, 0, 0),
          (0, 0, 0, 0),
          (0, 0, 0, 0)),

          ((0, 0, 0, 0),
          (0, 0, 0, 0),
          (0, 0, 0, 0),
          (0, 0, 0, 0)),

          ((0, 0, 0, 0),
          (0, 0, 0, 0),
          (0, 0, 0, 0),
          (0, 0, 0, 0)))
        - listed below are examples of initial boards you can run.


    - Finally, this prompt will display: ""Please enter the list of constraints or enter to skip.\n Accepted constraint symbols are: '>', '<', '^2', '^3', 'n', and 'nn'\nThe general format: (('symbol', (coordinate1), (coordinate2)),('symbol', (coordinate1), (coordinate2)), ... ('symbol', (coordinate1), (coordinate2)))"


       - enter the constraints you want to test with the board. For example, (('>', (0, 1, 1), (0, 1, 0)), ('>', (2, 2, 1), (2, 2, 0)))

# THE INITIAL BOARD:

the initial board's general format follows an array of an array of an array of a list of integers.
When entering the board, a '0' represents an empty initial cell.
For example, given an initial size of the board being 3, the initial board may be:

(((0, 0, 0),
(0, 0, 0),
(0, 0, 0)),

((0, 0, 0),
(0, 0, 0),
(0, 0, 0)),

((0, 0, 0),
(0, 0, 0),
(0, 0, 0)))

# CONSTRAINTS:

The general format: ('symbol', (coordinate1), (coordinate2)) where coordinate1 and coordinate2 follow (i, j, k).

    - i is for which "slice" of the matrix you want

    - j is for which row in the slice

    - k is for which column in the slice

# TO INPUT CONSTRAINTS:

(('symbol', (coordinate1), (coordinate2)),
('symbol', (coordinate1), (coordinate2)),
...
('symbol', (coordinate1), (coordinate2)))

Types of constraints are '>' '<' '^2' '^3' 'n' and 'nn'

- '>' means greater than. (coordinate1 > coordinate2)
  Ex. coordinate1 = 2 so coordinate1 is 1
  2 > 1

- '<' means less than. (coordinate1 < coordinate2)
  Ex. coordinate1 = 2 so coordinate1 is 3 or greater
  2 < 3... to size of num

- '^2' means coordinate1 squared is coordinate2. (coordinate1 ^2 coordinate2)
  Ex1. coordinate1 = 2 so coordinate2 must be 4
  2 ^2 4
  Ex2. coordinate1 = 3 so coordinate2 must be 9
  3 ^2 9

- '^3' means coordinate1 cubed is coordinate2. (coordinate1 ^3 coordinate2)
  Ex. coordinate1 = 2 so coordinate2 must be 8
  2 ^3 8

- 'n' means coordinate1's and coordinate2 are neighbors. A neighbor means they are + 1 or - 1 from each other (coordinate1 n coordinate2)
  Ex. coordinate1 = 2 so coordinate2 is either a 1 or 3
  2 n 1
  2 n 3
  \_ for end cases, such as 1 or the size of matrix, num, this wraps. the neighbor of 1 is 2 and the size of matrix (the max value)
  Ex. matrix size = 9 x 9 x 9
  1 n 9
  1 n 2

- 'nn' means coordinate1's and coordinate2 are non-neighbors. A non-neighbor means they can not be + 1 or - 1 from each other (coordinate1 nn coordinate2)
  Ex. coordinate1 = 2 so coordinate2 can not be either a 1 or 3
  2 n 5
  2 n 9
  \_ for end cases, such as 1 or the size of matrix, num, this wraps. the non neighbor of 1 is 2 and the size of matrix (the max value)
  Ex. matrix size = 9 x 9 x 9
  1 nn 7

# EXAMPLES OF INSTANCE INPUTS TO RUN:

These can be directly copied and pasted when running the file for the instance. You can change the 0 to values to see if it can be solved! The filled ones are just examples, you can make ones as well.

Empty 5 by 5 by 5 matrix:

(((0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0)),((0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0)),((0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0)),((0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0)),((0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0)),((0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0)))

Filled 5 by 5 by 5 matrix:

(((0,2,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,3,0,0,0)),((0,0,0,0,0,0),(5,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,4,0,0,0,0),(0,0,0,0,0,0)),((0,0,0,0,0,0),(0,0,0,1,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0)),((0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0)),((0,0,0,0,0,0),(0,5,0,0,0,0),(0,0,0,0,0,1),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0)),((0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,3,0,0,0),(1,0,0,0,0,0),(0,0,0,0,0,4)))

Empty 4 by 4 by 4 matrix:

(((0, 0, 0, 0),(0, 0, 0, 0),(0, 0, 0, 0),(0, 0, 0, 0)),((0, 0, 0, 0),(0, 0, 0, 0),(0, 0, 0, 0),(0, 0, 0, 0)),((0, 0, 0, 0),(0, 0, 0, 0),(0, 0, 0, 0),(0, 0, 0, 0)),((0, 0, 0, 0),(0, 0, 0, 0),(0, 0, 0, 0),(0, 0, 0, 0)))

Filled 4 by 4 by 4 matrix:

(((0, 0, 0, 0),(0, 0, 0, 0),(0, 0, 0, 0),(0, 3, 0, 0)),((0, 0, 0, 0),(0, 0, 0, 0),(0, 0, 0, 0),(0, 1, 0, 0)),((0, 0, 0, 0),(0, 0, 0, 0),(0, 0, 0, 2),(0, 0, 0, 0)),((1, 0, 0, 0),(0, 0, 0, 0),(0, 0, 0, 0),(0, 4, 0, 0)))

Empty 3 by 3 by 3 matrix:

(((0, 0, 0),(0, 0, 0),(0, 0, 0)), ((0, 0, 0),(0, 0, 0),(0, 0, 0)), ((0, 0, 0),(0, 0, 0),(0, 0, 0)))

Filled 3 by 3 by 3 matrix:

(((1, 0, 0),(0, 0, 0),(0, 0, 0)), ((0, 0, 0),(0, 0, 0),(0, 0, 0)), ((0, 0, 0),(0, 0, 0),(0, 0, 3)))

Empty 2 by 2 by 2 matrix:
(((0, 0),(0, 0)),((0, 0),(0, 0)))

# EXAMPLE OF CONSTRAINTS TO RUN:

These do depend on the size of the matrix instance given, but if running on any of the instances above should work. You can add to the list and try others if you'd like. These are compatible with size 3 or greater:

(('>', (0, 1, 1), (0, 1, 0)), ('<', (2, 2, 1), (2, 2, 0)))

(('>', (0, 1, 1), (0, 1, 0)), ('>', (2, 2, 1), (2, 2, 0)), ('n', (3, 1, 2), (3, 1, 3)), ('nn', (2, 2, 1), (1, 1, 1)))
