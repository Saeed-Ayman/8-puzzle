from typing import List, Tuple


class State:
    """
    A class to represent a state in a sliding puzzle game.

    Attributes:
    - Board (list[list[int]]):
        A 2D list of integers representing the board.

    - Direction (str):
        The direction of the empty space on the board.

    - EmptyPoint (dict):
        A dictionary representing the location of the empty space on the board.

    Methods:
    - __init__(
        board: list[list[int]],
        direction: str,
        emptyPoint: tuple[int, int]) -> None:
            Initializes a new State object with
            the given board, direction, and empty point.

    - __str__() -> str:
        Returns a string representation of the State object.
    """

    def __init__(
        self,
        board: List[List[int]],
        direction: str,
        emptyPoint: Tuple[int, int]
    ) -> None:
        """
        Initializes a new State object with
        the given board, direction, and empty point.

        Args:
        - board (list[list[int]]):
            A 2D list of integers representing the board.

        - direction (str):
            The direction of the empty space on the board.

        - emptyPoint (tuple[int, int]):
            A tuple representing the location of the empty space on the board.
        """
        self.Board = board
        self.Direction = direction
        self.EmptyPoint = {'X': emptyPoint[0], 'Y': emptyPoint[1]}

    def __str__(self) -> str:
        """
        Returns a string representation of the State object.

        Returns:
        - str:
            A string representation of the State object.
        """
        return '{{"Board": {0}, "Direction": "{1}", "EmptyPoint": {2}}}'.\
            format(self.Board, self.Direction, self.EmptyPoint)
