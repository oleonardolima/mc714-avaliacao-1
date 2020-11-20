from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def index_page():
    index_page = "<h1> Atividade #1 - MC732 - 2s2020<h1>\n"
    index_page += "<h2> Endereço de IP atual: {}<h2>\n".format(get_host_IP())
    return index_page

def get_host_IP():
    try:
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        return ip
    except:
        return "Não foi possível determinar o IP para o host atual\n"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")