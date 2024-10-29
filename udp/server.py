import socket
import math

SERVER_IP = '0.0.0.0'
SERVER_PORT = 5005
BUFFER_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

print("Servidor online!")

def eh_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def calcular(op1, op2, operacao):
    if operacao != "raiz" and (not op2 or not eh_numero(op2)):
        return "Erro: operação requer dois números"
    if not eh_numero(op1):
        return "Erro: Primeiro número inválido."

    op1 = float(op1)
    op2 = float(op2) if op2 else 0

    if operacao == "soma":
        return f"Resultado: {op1 + op2}"
    elif operacao == "subtracao":
        return f"Resultado: {op1 - op2}"
    elif operacao == "multiplicacao":
        return f"Resultado: {op1 * op2}"
    elif operacao == "divisao":
        return f"Resultado: {op1 / op2}" if op2 != 0 else "Erro: divisao por zero"
    elif operacao == "raiz":
        return f"Resultado: {math.sqrt(op1)}" if op1 >= 0 else "Erro: Raiz negativa"
    elif operacao == "potencia":
        return f"Resultado: {op1 ** op2}"
    else:
        return "Erro: Operação desconhecida"

try:
    while True:
        data, client_address = server_socket.recvfrom(BUFFER_SIZE)
        mensagem = data.decode().strip()

        argumentos = mensagem.split(';')
        if len(argumentos) != 3:
            resposta = "Erro: Formato inválido."
        else:
            op1, op2, operacao = argumentos
            if "encerra" in [op1.lower(), op2.lower(), operacao.lower()]:
                resposta = "Servidor encerrado!"
                server_socket.sendto(resposta.encode(), client_address)
                break

            if operacao == "raiz" and not op2:
                resposta = calcular(op1, op2, operacao)
            elif operacao != "raiz" and not op2:
                resposta = "Erro: A operação selecionada requer um segundo número."
            else:
                resposta = calcular(op1, op2, operacao)

        server_socket.sendto(resposta.encode(), client_address)

finally:
    print("Encerrando o servidor...")
    server_socket.close()
