import Pyro4 as pyro
from database import Database


@pyro.expose
class Menu:
    def __init__(self) -> None:
        self._products = Database.products

    @property
    def products(self):
        return self._products
