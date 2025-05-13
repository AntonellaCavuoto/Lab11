from dataclasses import dataclass


@dataclass()
class Vendite:
    pn1: int
    pn2: str
    date: str
    retailer: int

    def __hash__(self):
        pass





