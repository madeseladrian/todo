from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypedDict

class AddAccountParams(TypedDict):
    name: str
    email: str
    password: str

AddAccountOutput = bool

@dataclass
class AddAccount(ABC):

    @abstractmethod
    def add(self, account: AddAccountParams) -> AddAccountOutput:
        raise NotImplementedError('Should implement method: add')
