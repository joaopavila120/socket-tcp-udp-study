import socket
import math
import os

SERVER_IP = '0.0.0.0'
SERVER_PORT = 5005
BUFFER_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Permite reutilizar a porta
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(1)

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
    if not eh_numero(op2):
        return "Erro: segundo número inválido."

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
        conn, addr = server_socket.accept()
        data = conn.recv(BUFFER_SIZE).decode().strip()

        if "encerra" in data.lower():
            conn.send("Servidor encerrado!".encode())
            conn.close()
            os._exit(0)

        argumentos = data.split(';')
        if len(argumentos) != 3:
            resposta = "Erro: Formato inválido."
        else:
            op1, op2, operacao = argumentos
            if "encerra" in [op1.lower(), op2.lower(), operacao.lower()]:
                resposta = "Servidor encerrado!"
                conn.send(resposta.encode())
                conn.close()
                os._exit(0)

            if operacao != "raiz" and not op2:
                resposta = "Erro: A operação selecionada requer um segundo número."
            else:
                resposta = calcular(op1, op2, operacao)

        conn.send(resposta.encode())
        conn.close()

finally:
    server_socket.close()
