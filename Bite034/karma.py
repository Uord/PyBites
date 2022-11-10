from collections import namedtuple
from datetime import datetime

Transaction = namedtuple(
    "Transaction", "giver points date", defaults=(None, None, datetime.now())
)


class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self._transactions = []

    def __str__(self) -> str:
        return f"{self.name} has a karma of {self.karma} and {self.fans} fan{'s'[:self.fans^1]}"

    def __add__(self, other) -> None:
        self._transactions.append(other)

    @property
    def points(self) -> list:
        return [t.points for t in self._transactions]

    @property
    def karma(self) -> int:
        return sum(self.points)

    @property
    def fans(self) -> int:
        return len(set(t.giver.name for t in self._transactions))
