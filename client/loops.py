from view import View


class EventLoop:
    @staticmethod
    def login_loop(client):
        View.print_welcome()
        View.print_start_login()

        while True:
            credentials = View.get_credentials()
            is_valid = client.call_auth(credentials)

            if is_valid:
                View.print_success(0)
                return
            else:
                View.print_error(0)

    @staticmethod
    def menu_loop(client):
        done = True

        while done:
            menu = client.call_menu()
            View.print_menu(menu)

            order = View.get_order(menu, client._cache["registry"])
            if len(order["products"]) == 0:
                View.print_error(3)
                return

            order_is_posted = client.send_order(order)

            if order_is_posted is None:
                View.print_error(2)

            elif order_is_posted:
                View.print_success(1)

            else:
                View.print_error(1)

            done = View.print_new_order()
