# ATENÇÃO
# Para executar este main.py é necessário atualizar
# as localizações `<app>_location` das pastas
# onde os executaveis se encontram.

import os


def main():
    main_cmd = "C:\Windows\System32\cmd.exe /c start "

    pyro_name = main_cmd + '"Pyro Naming Server" '
    pyro_location = pyro_name + "/D C:\Data\Desenvolvimento\ADS "
    # pyro_server = pyro_location + "pyenv exec python -m Pyro4.naming"
    pyro_server = pyro_location + "python -m Pyro4.naming"

    server_name = main_cmd + '"Vitor Lopes Server" '
    server_location = server_name + "/D C:\Data\Desenvolvimento\ADS\Trabalho1\server "
    # my_server = server_location + "pyenv exec python main.py"
    my_server = server_location + "python main.py"

    client_name = main_cmd + '"Vitor Lopes Client" '
    client_location = client_name + "/D C:\Data\Desenvolvimento\ADS\Trabalho1\client "
    # my_client = client_location + "pyenv exec python main.py"
    my_client = client_location + "python main.py"

    service_name = main_cmd + '"Vitor Lopes Service" '
    service_location = service_name + \
        "/D C:\Data\Desenvolvimento\ADS\Trabalho1\service "
    # my_service = service_location + "pyenv exec python main.py"
    my_service = service_location + "python main.py"

    os.system(pyro_server)
    os.system(my_server)
    os.system(my_client)
    os.system(my_client)
    os.system(my_client)
    os.system(my_service)


if __name__ == '__main__':
    main()
