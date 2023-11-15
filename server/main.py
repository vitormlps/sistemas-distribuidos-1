from core import Core


def main():
    server = Core("localhost", 9090)
    server.serve()


if __name__ == '__main__':
    main()
