from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib

# Initialize server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 1911))
server_socket.listen(5)

# Generate RSA key pair
server_key = RSA.generate(2048)
list_of_connected_clients = []
clients = []

# Function to encrypt message
def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

# Function to decrypt message
def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

# Function to handle client connection
def handle_client(client_socket, client_address):
    print(f"Connected with {client_address}")
    
    # Send server's public key to client
    client_socket.send(server_key.publickey().export_key(format='PEM'))
    
    # Receive client's public key
    client_received_key = RSA.import_key(client_socket.recv(2048))
    
    # Generate AES key for encryption
    aes_key = get_random_bytes(16)
    
    # Encrypt the AES key using the client's public key
    cipher_rsa = PKCS1_OAEP.new(client_received_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)
    client_socket.send(encrypted_aes_key)
    
    # Add client to the list
    clients.append((client_socket, aes_key))
    
    while True:
        encrypted_message = client_socket.recv(2048)
        decrypted_message = decrypt_message(aes_key, encrypted_message)
        print(f"Received from {client_address}: {decrypted_message}")
        
        # Send received message to all other clients
        for client in clients:
            if client != (client_socket, aes_key):
                encrypted_message = encrypt_message(client[1], decrypted_message)
                client[0].send(encrypted_message)
        
        if decrypted_message == "exit":
            break
    
    clients.remove((client_socket, aes_key))
    print(f"Connection with {client_address} closed")
    client_socket.close()

# Accept and handle client connections
while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()