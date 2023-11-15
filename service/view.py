class View:
    @staticmethod
    def do_order(current_order):
        print("\nNovo pedido!!")
        print(
            f"\nCliente: {current_order['client']} \nPedido: {current_order['products']}")

        while True:
            choice_input = input('\nConfirma realização do pedido? (S/N) ')
            if choice_input in ["S", "s"]:
                print(
                    f"Dando baixa no pedido do cliente {current_order['client']}...")
                return True
            else:
                print("Cliente está esperando...")

    @staticmethod
    def print_success():
        print("Pedido realizado com sucesso!\n")

    @staticmethod
    def print_awaiting():
        print("Esperando por novos pedidos...", end="\r")

    @staticmethod
    def print_error(code):
        match code:
            case 0:
                print("Não foi possível realizar o pedido!\n")
            case 1:
                print("Houve um erro no pedido!\n")
