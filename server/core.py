import Pyro4 as pyro
from auth import Authentication
from menu import Menu
from order import Order


class Core:
    def __init__(self, host="localhost", port=9090) -> None:
        self._daemon = pyro.Daemon()
        self._name_server = pyro.locateNS(host=host, port=port)
        self._remote_objects = [Authentication, Menu, Order]

        self.register_objects()
        print(self._name_server.list())

    def register_objects(self):
        for obj in self._remote_objects:
            obj_uri = self._daemon.register(obj, objectId=obj.__name__)
            self._name_server.register(obj.__name__, obj_uri)

    def serve(self):
        return self._daemon.requestLoop()
