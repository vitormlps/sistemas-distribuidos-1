import Pyro4 as pyro


class Core:
    def __init__(self, host="localhost", port=9090) -> None:
        self._name_server = pyro.locateNS(host=host, port=port)
        self._remote_objects_names = ["Order"]
        self._proxies = self._build_proxies()
        self._cache = None
        self.order = self._call_(self._remote_objects_names[0])

    def _build_proxies(self):
        proxies = []

        for obj_name, obj_uri in self._name_server.list().items():
            if obj_name in self._remote_objects_names:
                proxies.append(pyro.Proxy(obj_uri))

        return proxies

    def _call_(self, remote_obj_name):
        for proxy in self._proxies:
            if remote_obj_name in proxy._pyroUri.asString():
                return proxy

    def call_order(self):

        if len(self.order.queue) == 0:
            self.order._pyroReconnect()
            return None

        return self.order.get_next()
