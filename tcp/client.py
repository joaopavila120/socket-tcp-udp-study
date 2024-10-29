import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5005

def eh_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def enviar_calculo(op1, op2, operacao):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        mensagem = f"{op1};{op2};{operacao}"
        client_socket.send(mensagem.encode())

        resposta = client_socket.recv(1024).decode()
        print(f"Resposta do servidor: {resposta}")
    except ConnectionRefusedError:
        print("Servidor não está mais disponível.")
    finally:
        client_socket.close()

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
