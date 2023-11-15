class View:
    @staticmethod
    def get_credentials():
        registry_input = input('Matricula: ').strip()
        password_input = input('Senha: ').strip()

        return {
            "registry": registry_input,
            "password": password_input
        }

    @staticmethod
    def get_order(menu, registry):
        print("\nDigite os produtos que deseja comprar (0 para realizar checkout):")
        products = []
        count = 1
        total_price = 0.0
        found = False

        while True:
            print("Valor atual: R$", total_price)
            choice_input = input(f'\nEscolha {count}: ').strip()

            if choice_input == "0":
                print("\nCHECKING OUT")
                print("Pedido:", products)
                print("Valor total: R$", total_price)
                break

            for item in menu:
                if choice_input == item["name"]:
                    total_price += item["price"]
                    found = True
                    break

            if found:
                products.append(choice_input)
                count += 1
            else:
                print("Produto não encontrado. Digite novamente:")

            found = False

        return {
            "client": registry,
            "products": products
        }

    @staticmethod
    def print_new_order():
        while True:
            choice_input = input('\nDeseja realizar um novo pedido? (S/N) ')
            if choice_input in ["S", "s"]:
                return True
            elif choice_input in ["N", "n"]:
                print("\nObrigado por utilizar nosso serviço. Até mais!")
                return False
            else:
                print("Valor digitado inválido! Digite novamente\n")

    @staticmethod
    def print_welcome():
        print("\nBem vindx a Cantina Monetizada!\n")

    @staticmethod
    def print_start_login():
        print("Digite sua matricula e senha para realizar o login")

    @staticmethod
    def print_menu(menu):
        print("\nAqui está o menu:")
        for item in menu:
            print(f'  {item["name"]} ... R${item["price"]}')

    @staticmethod
    def print_success(code):
        word = ""

        match code:
            case 0:
                word = "Login"
            case 1:
                word = "Pedido"

        print(f"{word} realizado com sucesso!")

    @staticmethod
    def print_error(code):
        match code:
            case 0:
                print("Matricula e/ou senha inválida!\n")
            case 1:
                print("Saldo insuficiente!\n")
            case 2:
                print("Houve um erro no seu pedido!")
            case 3:
                print("Nenhum pedido realizado!")
