import time
from view import View


class EventLoop:
    @staticmethod
    def main_loop(service):
        while True:
            current_order = service.call_order()

            if current_order is None:
                View.print_awaiting()

            else:
                done = View.do_order(current_order)

                if done:
                    View.print_success()

                else:
                    View.print_error(0)

            time.sleep(3)
