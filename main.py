import socket
import ssl
import threading

def server():
    server_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    server_socket.bind(("temp", 5))
    server_socket.listen(1)
    while True:
        client_socket, client_address = server_socket.accept()
        print(client_socket, client_address)
        secure_socket = context.wrap_socket(client_socket, server_side=True)
        data = secure_socket.recv(1024).decode()
        print(data)
        secure_socket.sendall(data.encode())

    

def client():
    client_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    client_socket.connect(("temp", 5))
    ssl_context = ssl.create_default_context(ssl.TLS_CLIENT)
    ssl_socket = ssl_context.wrap_socket(client_socket, server_hostname=server_mac_address)
    data_to_send = "Hello, Bluetooth!"
    ssl_socket.send(data_to_send.encode())
    print("sent")
    ssl_socket.close()
    client_socket.close()

server_thread = threading.Thread(target=server)
client_thread = threading.Thread(target=client)
server_thread.start()
client_thread.start()
server_thread.join()
client_thread.join()
