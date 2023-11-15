from core import Core
from loops import EventLoop


def main():
    service = Core("localhost", 9090)

    EventLoop.main_loop(service)


if __name__ == '__main__':
    main()
