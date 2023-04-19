# this main class in program
from Eight_Puzzle import Puzzle
from StatesPrinter import Printer

states = Puzzle(
    state=[
        [8, 3, 7],
        [1, 6, 0],
        [4, 2, 5]
    ],
    goal_state=[
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ],
    empty_position=(1, 2)
).solve()

Printer.print(states, True)
print(Printer.dir(states))
