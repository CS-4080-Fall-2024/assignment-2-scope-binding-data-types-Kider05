class RubiksCube:
    def __init__(self,size):
        self.size = size #class parameter size for different rubiks cube sizes
        self.faces = [
            [['W'] * size for _ in range(size)],  #white
            [['R'] * size for _ in range(size)],  #red
            [['B'] * size for _ in range(size)],  #blue
            [['O'] * size for _ in range(size)],  #orange
            [['G'] * size for _ in range(size)],  #green
            [['Y'] * size for _ in range(size)],  #yellow
            ]

    def display(self):
        for i, face in enumerate(self.faces):
            print(f"Face {i}:")
            for row in face:
                print(" ".join(row))
            print()

    def rotate_row(self, row_index, direction):

        #rotates a layer, layer_index = 0 for top, 1 for middle, 2 for bottom
        #direction parameter requires string 'clockwise' or 'counterclockwise'

        if direction not in ['right', 'left']: #checks for correct input
            print("Direction must be 'right' or 'left'.")

        face = self.faces[row_index]
        if direction == 'right':

            self.faces[row_index] = [list(reversed(col)) for col in zip(*face)]
        else:  #left

            self.faces[row_index] = [list(col) for col in reversed(list(zip(*face)))]

        if row_index == 0:  # Top layer
            self.rotate_adjacent_sides(row_index, direction, [1, 4, 3, 2])
        elif row_index == 2 or row_index == self.size:  # Bottom layer
            self.rotate_adjacent_sides(row_index, direction, [2, 3, 4, 1])

    def rotate_column(self, column_index, direction):
        # rotates a column, column_index = 0 for left, 1 for middle, 2 for right
        # direction parameter requires string 'up' or 'down'
        if direction not in ['up', 'down']:
            print("Direction must be 'up' or 'down'.")

        temp = []
        for i in range(self.size):
            temp.append(self.faces[0][i][column_index])  # Top face

        #rotate column
        if direction == 'down':
            for i in range(self.size):
                self.faces[0][i][column_index] = self.faces[1][i][column_index]  
                self.faces[1][i][column_index] = self.faces[5][i][column_index]
                self.faces[5][i][column_index] = self.faces[3][i][column_index]
                self.faces[3][i][column_index] = temp[i]  # Top face
        else:  # if direction == up
            for i in range(self.size):
                self.faces[3][i][column_index] = self.faces[5][i][column_index]
                self.faces[5][i][column_index] = self.faces[1][i][column_index]
                self.faces[1][i][column_index] = self.faces[0][i][column_index]
                self.faces[0][i][column_index] = temp[i]

    def rotate_adjacent_sides(self, row_index, direction, adjacent_faces):

        temp = [self.faces[i][row_index][:] for i in adjacent_faces]

        if direction == 'right':
            for i in range(len(adjacent_faces)):
                next_index = (i + 1) % len(adjacent_faces)
                self.faces[adjacent_faces[next_index]][row_index] = temp[i][:]
        else:  #left
            for i in range(len(adjacent_faces)):
                next_index = (i - 1) % len(adjacent_faces)
                self.faces[adjacent_faces[next_index]][row_index] = temp[i][:]


def user_interaction(cube):
    while True:
        print("Current cube state:")
        cube.display()

        action = input("Do you want to rotate a row or a column? (Enter 'row', 'column', or 'quit' to exit): ").strip().lower()
        if action == 'quit':
            print("Exiting the program.")
            break
        elif action == 'row':
            row_index = int(input("Enter the row index (0 for top, 1 for middle, 2 for bottom, etc): "))
            direction = input("Enter the direction ('right' or 'left'): ").strip().lower()
            cube.rotate_row(row_index, direction)
        elif action == 'column':
            column_index = int(input("Enter the column index (0 for left, 1 for middle, 2 for right, etc): "))
            direction = input("Enter the direction ('up' or 'down'): ").strip().lower()
            cube.rotate_column(column_index, direction)


num = int(input("what size rubiks cube do you want? Enter num for a numXnum cube\n"))
cube = RubiksCube(num)  # Create a 3x3 Rubik's Cube
user_interaction(cube)