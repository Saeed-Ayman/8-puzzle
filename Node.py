from State import State


class Node:
    """
    A class to represent a node in a search tree for a sliding puzzle game.

    Attributes:
    - state (list[list[int]]):
        A 2D list of integers representing the current state of the puzzle.

    - previous_state (str):
        A 2D list of integers converted to string representing
        the previous state key of the puzzle.

    - empty_position (tuple[int, int]):
        A tuple of integers representing
        the position of the empty square in the puzzle.

    - level (int):
        An integer representing the level of the node in the search tree.

    - cost (int):
        An integer representing the cost of the node.

    - dir (str):
        A string representing the direction of the move
        that led to this node from its parent node.

    Methods:
    - __init__(
        state: list[list[int]],
        previous_state: list[list[int]],
        empty_position: tuple[int, int],
        level: int,
        cost: int,
        dir: str) -> None:
        Initializes a new Node object with the given attributes.

    - fit() -> int:
        Calculates the fitness value of the node.

    - toState() -> State:
        Converts the node to a State object.
    """
    def __init__(
        self,
        state: list[list[int]],
        previous_state: str,
        empty_position: tuple[int, int],
        level: int,
        cost: int,
        dir: str
    ) -> None:
        """
        Initializes a new Node object with the given attributes.

        Args:
        - state (list[list[int]]):
            A 2D list of integers representing
            the current state of the puzzle.

        - previous_state str:
            A 2D list of integers converted to string representing
            the previous state key of the puzzle.

        - empty_position (tuple[int, int]):
            A tuple of integers representing
            the position of the empty square in the puzzle.

        - level (int):
            An integer representing the level of the node in the search tree.

        - cost (int):
            An integer representing the cost of the node.

        - dir (str):
            A string representing the direction of the move
            that led to this node from its parent node.
        """
        self.state: list[list[int]] = state
        self.previous_state: str = previous_state
        self.empty_position: tuple[int, int] = empty_position
        self.level: int = level
        self.cost: int = cost
        self.dir: str = dir

    def fit(self) -> int:
        """
        Calculate the fitness value of the node.

        Returns:
            An integer representing the fitness value of the node.
        """
        return self.level + self.cost

    def toState(self) -> State:
        """
        Converts the node to a State object.

        Returns:
        - State:
            A new State object created from the current Node object.
        """
        return State(self.state, self.dir, self.empty_position)
