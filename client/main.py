from core import Core
from loops import EventLoop


def main():
    client = Core("localhost", 9090)

    EventLoop.login_loop(client)
    EventLoop.menu_loop(client)


if __name__ == '__main__':
    main()
