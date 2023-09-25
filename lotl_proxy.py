import binascii
import socket
import struct

def lotl_proxy(src,dest):
    src_sock = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(3))
    src_sock.bind((src,0))
    dest_sock = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(3))
    dest_sock.bind((dest,0))

    while True:
        init_src_data = src_sock.recv(65536)
        src_data = binascii.hexlify(init_src_data[0:6]) + binascii.hexlify(init_src_data[6:len(init_src_data)])
        dest_sock.sendall(binascii.unhexlify(src_data))
        
        init_dest_data = dest_sock.recv(65536)
        dest_data = binascii.hexlify(init_dest_data[0:6]) + binascii.hexlify(init_dest_data[6:12]) + binascii.hexlify(init_dest_data[12:len(init_src_data)])
        src_sock.sendall(binascii.unhexlify(dest_data))

lotl_proxy("eth0","tun0")
