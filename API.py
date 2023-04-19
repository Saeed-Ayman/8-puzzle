from json import dumps, loads
from State import State


class Api:
    """
    A class that provides methods for encoding and decoding
    States to and from JSON strings.

    Methods:
    - Encode(states: list[State]) -> str:
        Encodes a list of State objects to a JSON string.

    - Decode(jsonString: str) -> State:
        Decodes a JSON string to a State object.
    """
    def Encode(states: list[State]) -> str:
        """
        Encodes a list of State objects to a JSON string.

        Args:
        - states (list[State]):
            A list of State objects to encode.

        Returns:
        - str:
            A JSON string representing the list of State objects.
        """
        return dumps([state.__dict__ for state in states])

    def Decode(jsonString: str) -> State:
        """
        Decodes a JSON string to a State object.

        Args:
        - jsonString (str):
            A JSON string to decode.

        Returns:
        - State:
            A State object representing the decoded JSON string.
        """
        obj = loads(jsonString)
        return State(
            obj['Board'],
            obj['Direction'],
            (obj['EmptyPoint']['X'], obj['EmptyPoint']['Y'])
        )
