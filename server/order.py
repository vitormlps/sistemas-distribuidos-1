import Pyro4 as pyro
from database import Database


@pyro.expose
@pyro.behavior(instance_mode="single")
class Order:
    def __init__(self) -> None:
        self.order_queue = []

    @property
    def queue(self):
        return self.order_queue

    def get_next(self):
        return self.order_queue.pop(0)

    def post_order(self, client_registry, order_products):
        current_balance = 0
        current_products = []

        for client in Database.clients:
            if client_registry == client["registry"]:
                current_balance = client["balance"]

        temp_balance = current_balance

        for prod_name in order_products:
            for product in Database.products:
                if prod_name == product["name"]:
                    temp_balance -= product["price"]
                    if temp_balance < 0:
                        return False
                    else:
                        current_balance -= product["price"]
                        current_products.append(product)

        for client in Database.clients:
            if client_registry == client["registry"]:
                client["balance"] = current_balance

        self.order_queue.append(
            {"client": client_registry, "products": current_products})

        print(self.order_queue)

        return True
