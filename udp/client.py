import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5005

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def eh_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def enviar_calculo(op1, op2, operacao):
    mensagem = f"{op1};{op2};{operacao}"
    client_socket.sendto(mensagem.encode(), (SERVER_IP, SERVER_PORT))

    try:
        resposta, _ = client_socket.recvfrom(1024)
        print(f"Resposta do servidor: {resposta.decode()}")
        if "Servidor encerrado" in resposta.decode():
            print("Servidor foi encerrado.")
            client_socket.close()
            exit()
    except:
        print("")

while True:
    op1 = input("Digite o primeiro valor (ou 'encerra' para sair): ")
    if "encerra" in op1.lower():
        enviar_calculo(op1, '', '')
        break

    op2 = input("Digite o segundo valor (caso nao precise deixe vazio): ")
    if "encerra" in op2.lower():
        enviar_calculo(op1, op2, '')
        break

    operacao = input("Digite a operacao em um desses formatos: soma, subtracao, multiplicacao, divisao, raiz, potencia: ")
    if "encerra" in operacao.lower():
        enviar_calculo(op1, op2, operacao)
        break

    if not eh_numero(op1):
        print("Erro: Primeiro valor inválido. Digite um número.")
        continue
    if operacao != "raiz" and not op2:
        print("Erro: A operação selecionada requer um segundo valor.")
        continue
    if operacao != "raiz" and not eh_numero(op2):
        print("Erro: Segundo valor inválido. Digite um número.")
        continue

    enviar_calculo(op1, op2, operacao)

client_socket.close()
