import Pyro4 as pyro
from database import Database


@pyro.expose
class Authentication:

    @staticmethod
    def validate_(credentials):
        found = False

        for client in Database.clients:
            if credentials["registry"] == client["registry"] and \
                    credentials["password"] == client["password"]:
                found = True
                break

        if found:
            print(f"Login: {credentials['registry']}")
        else:
            print("Tentativa de login: credenciais inválidas")

        return found
