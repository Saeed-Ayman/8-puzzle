from Node import Node
from copy import deepcopy
from State import State


class Puzzle:
    """
    A class to represent a solver for a sliding puzzle game.
    The sliding puzzle is represented as a 2D array of integers,
    where one of the values is an empty space that can be
    slid in one of four directions (up, down, left, right)
    to swap places with an adjacent non-empty space.

    Attributes:
    - DIRECTIONS dict[str, List[int]]:
        Adds those changes to the current position to get the new position.

    - goal_state (list[list[int]]):
        A 2D list of integers representing the goal state of the puzzle.

    - open_set (dict[str, Node]):
        A set of nodes that have been discovered but have not yet been visited.

    - closed_set (dict[str, Node]):
        A set of nodes that have already been visited.
        These nodes have already been explored and
        their neighbors have been added to the open_set.

    Methods:
    - __init__(
        state: list[list[int]],
        goal_state: list[list[int]],
        empty_position: tuple[int, int]
    ) -> None:
        Initialize a PuzzleSolver object.

    - def get_pos(self, element) -> tuple[int, int]:
        Get the position of an element in the goal state.

    - def euclideanCost(self, state) -> int:
        Calculate the Euclidean cost of a given state.

    - def getAdjNode(self, node: Node) -> list[Node]:
        Get a list of adjacent nodes for a given node.

    - def getBestNode(self) -> Node:
        Get the node with the lowest fit value in the open set.

    - def buildPath(self) -> list[State]:
        Build the path to the goal state.

    - def solve(self):
        Find the path from the initial state to the goal state.
        this function is considered a main function in this class.
    """
    DIRECTIONS = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}

    def __init__(
        self,
        state: list[list[int]],
        goal_state: list[list[int]],
        empty_position: tuple[int, int]
    ) -> None:
        """
        Initialize a PuzzleSolver object.

        Args:
            state:
                a 2D list of integers representing
                the initial state of the puzzle.

            goal_state:
                a 2D list of integers representing
                the goal state of the puzzle.

            empty_position:
                a tuple of integers representing
                the position of the empty square in the puzzle.
        """
        self.goal_state: list[list[int]] = goal_state
        self.open_set: dict[str, Node] = {
            str(state): Node(
                state=state,
                previous_state=None,
                empty_position=empty_position,
                level=0,
                cost=self.euclideanCost(state=state),
                dir=""
            )
        }
        self.closed_set: dict[str, Node] = {}

    def get_pos(self, element) -> tuple[int, int]:
        """
        Get the position of an element in the goal state.

        Args:
            element:
                an integer representing the element to find in the goal state.

        Returns:
            A tuple of integers representing the row and column
            indices of the element in the goal state.

        Raises:
            Exception:
                if the element is not present in the goal stat
        """
        for row in range(len(self.goal_state)):
            if element in self.goal_state[row]:
                return (row, self.goal_state[row].index(element))
        raise Exception("Array Not The Same Variable")

    def euclideanCost(self, state) -> int:
        """
        Calculate the Euclidean cost of a given state.

        The Euclidean cost is the sum of the Euclidean distances
        between each tile and its goal position.

        Args:
            state:
                a 2D list of integers representing
                the state to calculate the cost for.

        Returns:
            An integer representing the Euclidean cost of the state.
        """
        cost = 0
        for row in range(len(state)):
            for col in range(len(state[0])):
                pos = self.get_pos(state[row][col])
                cost += abs(row - pos[0]) + abs(col - pos[1])
        return cost

    def getAdjNode(self, node: Node) -> list[Node]:
        """
        Get a list of adjacent nodes for a given node.

        Args:
            node:
                a Node object representing
                the node to get adjacent nodes for.

        Returns:
            A list of Node objects representing the adjacent nodes.
        """
        listNode: list[Node] = list()
        empty_position: tuple[int, int] = node.empty_position

        for dir in self.DIRECTIONS.keys():
            newPos = (
                empty_position[0] + self.DIRECTIONS[dir][0],
                empty_position[1] + self.DIRECTIONS[dir][1]
            )
            if 0 <= newPos[0] < len(node.state) and \
                    0 <= newPos[1] < len(node.state[0]):
                newState = deepcopy(node.state)
                newState[empty_position[0]][empty_position[1]] = \
                    node.state[newPos[0]][newPos[1]]
                newState[newPos[0]][newPos[1]] = \
                    node.state[empty_position[0]][empty_position[1]]
                listNode.append(
                    Node(
                        state=newState,
                        previous_state=str(node.state),
                        empty_position=newPos,
                        level=node.level + 1,
                        cost=self.euclideanCost(newState),
                        dir=dir
                    )
                )
        return listNode

    def getBestNode(self) -> Node:
        """
        Get the node with the lowest fit value in the open set.

        The fit value is a combination of the level and cost of the node.

        Returns:
            The Node object with the lowest fit value.
        """
        best_fit: Node = None
        for node in self.open_set.values():
            if best_fit is None or node.fit() < best_fit.fit():
                best_fit = node
        return best_fit

    def buildPath(self) -> list[State]:
        """
        Build the path to the goal state.

        Returns:
            A list of dictionaries representing
            the path to the goal state. Each dictionary contains
            the direction moved, new state, and empty position.
        """
        node: Node = self.closed_set[str(self.goal_state)]
        branch = list()

        while node.previous_state is not None:
            branch.append(node.toState())
            node = self.closed_set[node.previous_state]

        branch.append(node.toState())
        branch.reverse()

        return branch

    def solve(self):
        """
        Find the path from the initial state to the goal state.

        Returns:
            A list of dictionaries representing
            the path to the goal state. Each dictionary contains
            the direction moved, new state, and empty position.
        """
        while True:
            best_node: Node = self.getBestNode()
            if best_node is None:
                raise Exception("Can Not Solve This State.")
            key_best_node = str(best_node.state)
            self.closed_set[key_best_node] = best_node

            if best_node.state == self.goal_state:
                return self.buildPath()

            for node in self.getAdjNode(best_node):
                key = str(node.state)
                if key in self.closed_set.keys() or \
                        key in self.open_set.keys() and \
                        self.open_set[key].fit() < node.fit():
                    continue
                self.open_set[key] = node

            del self.open_set[key_best_node]
