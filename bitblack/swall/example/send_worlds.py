import socket


def stream_serve():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 9999))
    server.listen(3)
    conn, address = server.accept()
    print(address)
    conn.send("hello world\n")
    conn.close()
    server.close()


stream_serve()
