import Pyro4 as pyro


class Core:
    def __init__(self, host="localhost", port=9090) -> None:
        self._name_server = pyro.locateNS(host=host, port=port)
        self._remote_objects_names = ["Authentication", "Menu", "Order"]
        self._proxies = self._build_proxies()
        self._cache = None

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

    def call_auth(self, credentials):
        self._cache = credentials

        with self._name_server:
            auth = self._call_(self._remote_objects_names[0])
            is_valid = auth.validate_(credentials)

        return is_valid

    def call_menu(self):
        with self._name_server:
            menu = self._call_(self._remote_objects_names[1])
        return menu.products

    def send_order(self, order_data):
        with self._name_server:
            order = self._call_(self._remote_objects_names[2])
            order_is_posted = order.post_order(
                order_data["client"], order_data["products"])
        return order_is_posted
