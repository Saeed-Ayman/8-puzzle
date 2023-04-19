from State import State
from msvcrt import getche
# unicode for draw puzzle in command prompt or terminal
EDGE = {
    "LD": '\u2514',
    "RD": '\u2518',
    "RU": '\u2510',
    "LU": '\u250C'
}
CROSS = {
    "M": '\u253C',
    "T": '\u252C',
    "B": '\u2534',
    "R": '\u2524',
    "L": '\u251C'
}
BAR = '\u2502'
DASH = '\u2500'
# Line draw code
LINE = [
    i + 2 * (3 * DASH + j) + 3 * DASH + k
    for i, j, k in zip(
        [EDGE["LU"], CROSS["L"], EDGE["LD"]],
        [CROSS["T"], CROSS["M"], CROSS["B"]],
        [EDGE["RU"], CROSS["R"], EDGE["RD"]]
    )
]


class Printer:
    """Class print state in console with some shapes
    Methods:
    - def print_puzzle(state, p):
        Print the current state of the puzzle.

    - def total_steps(states: list[State]):
        Get the total number of steps in the solution.

    - def print(states: list[State], pressKeyToContinue: bool):
        Print the steps taken to solve the puzzle.
        this function is considered a main function in this class.
    """
    def print_puzzle(state, p):
        """
        Print the current state of the puzzle.

        Args:
            state: A 2D list representing the current state of the puzzle.

            p: A tuple representing the position of the empty tile.
        """
        print(LINE[0])
        for a in range(len(state)):
            print(*[f'{BAR} {i if i != state[p["X"]][p["Y"]] else " "}'
                    for i in state[a]], BAR)
            print(LINE[2 if a == len(state) - 1 else 1])

    def total_steps(states: list[State]):
        """
        Get the total number of steps in the solution.

        Returns:
            An integer representing the total number of steps in the solution.
        """
        return len(states) - 1

    def print(states: list[State], pressKeyToContinue: bool):
        """ Print the steps taken to solve the puzzle. """
        print(2 * DASH + CROSS["R"], "INPUT", CROSS["L"] + 2 * DASH)
        for state in states:
            if state.Direction != '':
                print(
                    4 * DASH + CROSS["R"],
                    state.Direction,
                    CROSS["L"] + 4 * DASH
                )
            Printer.print_puzzle(state.Board, state.EmptyPoint)
            # Wait for a key press before printing the next step.
            # Clear the printed state of the puzzle
            # and move the cursor back to the start of the line
            if pressKeyToContinue:
                getche()
                print('\r\b ')
        print('total steps : ', Printer.total_steps(states), end="\n\n")

    def dir(states: list[State]) -> list[str]:
        return [state.Direction for state in states]
