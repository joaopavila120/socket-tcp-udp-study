
# UDP and TCP Calculator: Python Client-Server Interaction

This project implements a simple client-server calculator in Python using both **UDP** and **TCP** protocols. Each version of the calculator is capable of receiving two numerical arguments and an operation command from the client, returning the result or an error message when necessary. The server can also be terminated by a command from the client.

## Project Structure

The project is organized into two main directories:
- **`tcp/`**: Contains the TCP implementation of the client-server calculator.
  - `server.py`: TCP server that performs calculations and handles client requests.
  - `client.py`: TCP client that sends calculation requests to the server.
- **`udp/`**: Contains the UDP implementation of the client-server calculator.
  - `server.py`: UDP server that performs calculations and handles client requests.
  - `client.py`: UDP client that sends calculation requests to the server.

## Supported Operations

The calculator supports the following operations:
1. **Addition** (`soma`): Adds the two operands.
2. **Subtraction** (`subtracao`): Subtracts the second operand from the first.
3. **Multiplication** (`multiplicacao`): Multiplies the two operands.
4. **Division** (`divisao`): Divides the first operand by the second. Returns an error if the second operand is zero.
5. **Square Root** (`raiz`): Calculates the square root of the first operand. Allows the second operand to be empty.
6. **Exponentiation** (`potencia`): Raises the first operand to the power of the second.
7. **Terminate Server** (`encerra`): Closes the server when received from the client.

## Requirements

- Python 3.6 or higher
