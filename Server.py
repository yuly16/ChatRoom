import socket
import select
host = ""
port = 8000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)
r_list = [server, ]
w_list = []
socket2name = {}
while r_list:
    inputs, _, _ = select.select(r_list, w_list, r_list)
    # new client
    for input in inputs:
        if input is server:

            # accept the socket of client
            sock, addr = input.accept()
            new_fd = sock.getpeername()[1]

            # acquire the name of client
            name = sock.recv(1024)
            socket2name[sock] = name

            # # send "login success message" to the client

            r_list.append(sock)
            print("got connection from ", sock.getpeername(), ' its name is %s'%(str(name,encoding='utf-8')))
            for client in r_list[1:]:
                client.send(name + bytes(' joins the chat room.', encoding='utf-8'))
        else:
            try:
                msg = input.recv(1024)
                msg_str = str(msg, encoding='utf-8')
                print(msg_str)
                if msg == b'':
                    input.close()
                    r_list.remove(input)
                    name = socket2name[input]
                    for client in r_list[1:]:
                        client.send(name + bytes(' leaves the chat room', encoding='utf-8'))
                else:
                    # broadcast the message
                    sender_name = socket2name[input] + bytes(': ', encoding='utf-8')
                    for client in r_list[1:]:
                        client.send(sender_name + msg)
            except socket.error:
                r_list.remove(input)
                name = socket2name[input]
                for client in r_list[1:]:
                    client.send(name + bytes(' leaves the chat room', encoding='utf-8'))



