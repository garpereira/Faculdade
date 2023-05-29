from rc4 import RC4

import sys
import os
import subprocess
from PyQt5.QtNetwork import QTcpServer, QTcpSocket, QAbstractSocket
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
from ctypes import *
import ctypes
import socket
from random import randint

class Validator(QRegExpValidator):
    def __init__(self, pattern):
        super().__init__(QRegExp(f"[{pattern}]+"))


class mainWindow(QMainWindow):

    __instancia__ = None

    def __init__(self):
        super().__init__()
        screen_geo = QDesktopWidget().availableGeometry()
        x = (screen_geo.width() - self.width()) / 2
        y = (screen_geo.height() - self.height()) / 2

        self.setGeometry(x, y, 400, 600) #posicao x, y, largura, altura
        self.setWindowTitle('Telegram da DeepWeb')
        icone = QIcon('./tuiterr.png')
        self.setWindowIcon(icone)

        # Pegando o IP LOCAL
        #self.MyHN = socket.gethostname()
        self.MyIP = self.get_local_ip()

        # Objeto Servidor
        self.Servidor = QTcpServer()
        self.Servidor.newConnection.connect(self.handle_connection)

        # Objeto Cliente
        self.Cliente = QTcpSocket()
        self.Cliente.readyRead.connect(self.recebeMsg_Cliente)

        # Lista de cores
        self.msgColors = {}

        # Compilando os Codigos C
        self.compilaCodigos()

        # Campo de IP ORIGEM
        self.seu_IP_label = QLabel(self)
        self.seu_IP_label.setText('IP LOCAL')
        self.seu_IP_label.setGeometry(10, 1, 120, 10)
        self.seu_IP_label.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(5)
        self.seu_IP_label.setFont(font)

        self.local_IP = QLineEdit(self)
        self.local_IP.setPlaceholderText(str(self.MyIP))
        self.local_IP.setGeometry(10, 10, 120, 30)
        self.local_IP.setReadOnly(True)

        # Campo de IP DESTINO
        self.text_IP = QLineEdit(self)
        self.text_IP.setPlaceholderText('Digite o IP Destino')
        self.text_IP.setGeometry(10, 60, 120, 30)
        #self.text_IP.textChanged.connect()

        # Campo de PORTA SERVIDOR DESTINO
        self.text_PORT_Destino = QLineEdit(self)
        self.text_PORT_Destino.setPlaceholderText("Porta Destino")
        self.text_PORT_Destino.setGeometry(135, 60, 85, 30)

        # Botão Conectar Cliente
        self.btn_Conectar = QPushButton('Conectar', self)
        self.btn_Conectar.setGeometry(290, 60, 100, 30)
        self.btn_Conectar.clicked.connect(lambda : self.conectar())

        # Botão Ligar Servidor
        self.btn_LigarServidor = QPushButton('Ligar Servidor', self)
        self.btn_LigarServidor.setGeometry(290, 10, 100, 30)
        self.btn_LigarServidor.clicked.connect(lambda : self.start())

        # Campo de PORTA SERVIDOR
        self.text_PORT_Local = QLineEdit(self)
        self.text_PORT_Local.setPlaceholderText("Porta Local")
        self.text_PORT_Local.setGeometry(135, 10, 85, 30)
        
        # Campo de CHAVE CRIPTOGRAFADORA
        self.text_KEY = QLineEdit(self)
        self.text_KEY.setPlaceholderText('Digite a Chave Cripto')
        self.text_KEY.setGeometry(10, 110, 275, 30)
        #self.text_KEY.setMaxLength(10)
        #self.text_KEY.setValidator(QIntValidator(self))

        # Caixa de Seleção do Algoritmo
        self.opt_ALGORITHMS = QComboBox(self)
        self.opt_ALGORITHMS.addItems(['RC4', 'SDES'])
        self.opt_ALGORITHMS.setGeometry(290, 110, 100, 30)
        self.opt_ALGORITHMS.currentIndexChanged.connect(self.updateTypeKEY)
        #default_index = self.opt_ALGORITHMS.findText('RC4')
        #self.opt_ALGORITHMS.setCurrentIndex(default_index)

        # Titulo do Chat
        self.text_MSGCHAT_LABEL = QLabel(self)
        self.text_MSGCHAT_LABEL.setText('BATE PAPO UOL')
        self.text_MSGCHAT_LABEL.setGeometry(10, 150, 380, 30)
        self.text_MSGCHAT_LABEL.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(15)
        self.text_MSGCHAT_LABEL.setFont(font)

        # Chat 1
        self.text_MSGCHAT = QTextEdit(self)
        self.text_MSGCHAT.setGeometry(10, 180, 380, 130)
        self.text_MSGCHAT.setReadOnly(True)

        # Adicionar sombra nas bordas
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(5)  # Definir o raio de desfoque da sombra
        shadow_effect.setColor(QColor(0, 0, 0, 150))  # Definir a cor da sombra
        shadow_effect.setOffset(0, 0)  # Definir o deslocamento da sombra
        self.text_MSGCHAT.setGraphicsEffect(shadow_effect)
        
        scrollbar = QScrollBar(self)
        scrollbar.setGeometry(380, 200, 20, 300)
        self.text_MSGCHAT.setVerticalScrollBar(scrollbar)

        # Titulo do Chat 2
        self.text_MSGCHAT_LABEL = QLabel(self)
        self.text_MSGCHAT_LABEL.setText('CRIPTOGRAFADO')
        self.text_MSGCHAT_LABEL.setGeometry(10, 330, 380, 30)
        self.text_MSGCHAT_LABEL.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(15)
        self.text_MSGCHAT_LABEL.setFont(font)

        # Chat 2
        self.text_MSGCHAT_CRIPTO = QTextEdit(self)
        self.text_MSGCHAT_CRIPTO.setGeometry(10, 360, 380, 130)
        self.text_MSGCHAT_CRIPTO.setReadOnly(True)

        # Adicionar sombra nas bordas
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(5)  # Definir o raio de desfoque da sombra
        shadow_effect.setColor(QColor(0, 0, 0, 150))  # Definir a cor da sombra
        shadow_effect.setOffset(0, 0)  # Definir o deslocamento da sombra
        self.text_MSGCHAT_CRIPTO.setGraphicsEffect(shadow_effect)
        
        scrollbar = QScrollBar(self)
        scrollbar.setGeometry(380, 200, 20, 300)
        self.text_MSGCHAT_CRIPTO.setVerticalScrollBar(scrollbar)

        # Campo de enviar a mensagem
        self.text_MSG = QLineEdit(self)
        self.text_MSG.setPlaceholderText('Escreva sua mensagem')
        self.text_MSG.setGeometry(10, 520, 275, 30)
        self.text_MSG.installEventFilter(self)
        #self.text_MSG.setValidator(QIntValidator(self))
        #self.text_MSG.setMaxLength(8)

        # Botão Enviar mensagem
        self.btn_Enviar = QPushButton('Enviar', self)
        self.btn_Enviar.setGeometry(290, 520, 100, 30)
        self.btn_Enviar.clicked.connect(lambda: self.enviar_mensagem('servidor', self.opt_ALGORITHMS.currentText()))
    
# SERVIDOR
######################################
    def start(self):
        if self.text_PORT_Local.text() == "":
            self.notify_box("Porta Local")
            return
        if not self.Servidor.listen(port=int(self.text_PORT_Local.text())):
            print("Falha ao iniciar o servidor")
            sys.exit()

        print("Servidor iniciado e aguardando conexões...")

    def handle_connection(self):
        try:
            print("entrou no try do handle")
            self.client_socket = self.Servidor.nextPendingConnection()
            self.client_socket.readyRead.connect(lambda: self.receive_message(self.client_socket))
            self.client_socket.disconnected.connect(lambda: self.disconnect_client(self.client_socket))
        except:
            print("pulou pro except do handle")
            #self.client_socket
            self.client_socket.readyRead.connect(lambda: self.receive_message(self.client_socket))
            self.client_socket.disconnected.connect(lambda: self.disconnect_client(self.client_socket))

        print("Novo cliente conectado:", self.client_socket.peerAddress().toString())

    def receive_message(self, client_socket):
        print("entrou no receive_message")
        message = client_socket.readAll().data()
        print("Mensagem recebida de", client_socket.peerAddress().toString(), ":", message)

        # Mensagem recebida, entao vai Decriptar
        self.decripta_GLOBAL(self.text_KEY.text(), message, client_socket.peerAddress().toString(), self.opt_ALGORITHMS.currentText())
        print("decriptou depois que recebeu no servidor")

        # Envie a mensagem para todos os outros clientes conectados
        #for client in self.Servidor.children():
        #   if isinstance(client, QAbstractSocket) and client != client_socket:
        #       client.write(message.encode())

    def disconnect_client(self, client_socket):
        print("Cliente desconectado:", client_socket.peerAddress().toString())
        client_socket.deleteLater()


# CLIENTE
####################################
    def conectar(self):
        if self.text_IP.text() == "":
            self.notify_box("IP Destino.")
            return
        if self.text_PORT_Destino.text() == "":
            self.notify_box("Porta Destino")
            return
        self.Cliente.connectToHost(str(self.text_IP.text()), int(self.text_PORT_Destino.text()))

    def recebeMsg_Cliente(self):
        mensagem_ = self.Cliente.readAll().data()
        self.decripta_GLOBAL(self.text_KEY.text(), mensagem_, self.Cliente.peerAddres().toString(), self.opt_ALGORITHMS.currentText())
        
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress and obj is self.text_MSG:
            if event.key() == Qt.Key_Return:
                self.enviar_mensagem('servidor', self.opt_ALGORITHMS.currentText())
                return True
            return False
        
        return False

    def updateTypeKEY(self):
        OPT = self.opt_ALGORITHMS.currentText()
        #regex3 = QRegExp("^[01]+")
        #validador3 = QRegExpValidator(regex3, self)
        #validator = QRegularExpressionValidator("[01]+")

        if OPT == 'SDES':
            print("mudou pra SDES")
            # default_index = self.opt_ALGORITHMS.findText('SDES')
            # self.opt_ALGORITHMS.setCurrentIndex(default_index)
            self.text_KEY.clear()
            self.text_KEY.setValidator(Validator("01"))
            self.text_KEY.setMaxLength(10)

            self.text_MSG.clear()
            self.text_MSG.setValidator(Validator("01"))
            self.text_MSG.setMaxLength(8)
            
        elif OPT == 'RC4':
            print("mudou pra RC4")
            # default_index = self.opt_ALGORITHMS.findText('RC4')
            # self.opt_ALGORITHMS.setCurrentIndex(default_index)
            self.text_KEY.clear()
            self.text_KEY.setValidator(None)
            self.text_KEY.setMaxLength(256)

            self.text_MSG.clear()
            self.text_MSG.setValidator(None)
            self.text_MSG.setMaxLength(256)

    def printaERRO(self, resultado):
        if resultado.returncode == 0:
            print("Compilação bem-sucedida.")
        else:
            print("Ocorreu um erro durante a compilação.")
            print("Saída de erro:", resultado.stderr)

    def get_local_ip(self):
        try:
            # Cria um socket para obter o IP local
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.connect(("8.8.8.8", 80))  # Conecta a um servidor externo (Google DNS)

            # Obtém o endereço IP local
            local_ip = sock.getsockname()[0]

            # Fecha o socket
            sock.close()

            return local_ip
        except socket.error:
            return None
    
    def compilaCodigos(self):
        comandos = [
            ['gcc', '-shared', '-o', 'sdes.so', '-fPIC', 'sdes.c']
            #['gcc', '-shared', '-o', 'rc4.so', '-fPIC', 'rc4.c']
        ]
        paths = ['sdes/']#, 'rc4/']

        for i in range(len(comandos)):
            original_path = os.getcwd()
            os.chdir(paths[i])
            resultado = subprocess.run(comandos[i], capture_output=True, text=True)
            self.printaERRO(resultado)
            os.chdir(original_path)

        try:
            self.so_des = "./sdes/sdes.so"
            self.sdes_functions = CDLL(self.so_des)

            # self.so_rc4 = "./rc4/rc4.so"
            # self.rc4_functions = CDLL(self.so_rc4)
            # self.rc4_functions.argtypes = [
            #     c_char_p,  # key
            #     c_char_p,  # plaintext
            #     ctypes.POINTER(ctypes.c_ubyte), # ciphertext
            #     ctypes.c_int
            # ]
            # self.rc4_functions.restype = None

        except:
            print("deu ruim padrin")
            None

    def decripta_GLOBAL(self, chave_, mensagem_cripto, cliente_ip, opt_algoritmo):
        if opt_algoritmo == 'SDES':
            print(f'MsgCriptSDES Python -> {mensagem_cripto.decode()}\n')
            buffer = create_string_buffer(8)
            self.sdes_functions.dcript(chave_.encode(), mensagem_cripto, buffer)
            mensagem_dcripto = buffer.value.decode()
            print(f'MsgDCriptSDES Python -> {mensagem_dcripto}\n')
            self.envia_mensagemCHAT(mensagem_cripto.decode(), mensagem_dcripto, cliente_ip)

        if opt_algoritmo == 'RC4':
            #mensagem_cripto = ":".join(mensagem_cripto.hex()[i:i+2] for i in range(0, len(mensagem_cripto.hex()), 2))
            print(f'MsgCriptRC4 Python -> {mensagem_cripto.hex()}\n')
            mensagem_dcripto = RC4(chave_.encode(), mensagem_cripto).decode()
            print(f'MsgDCriptRC4 Python -> {mensagem_dcripto}\n')
            self.envia_mensagemCHAT(mensagem_cripto.hex(), mensagem_dcripto, cliente_ip)
            

    def envia_mensagemCHAT(self, mensagem_cripto, mensagem_dcripto, cliente_ip):
        R = randint(0, 255)
        G = randint(0, 255)
        B = randint(0, 255)

        print("veio pra enviar pro chat")
        
        if cliente_ip not in self.msgColors:
            self.msgColors[cliente_ip] = QColor(R,G,B)

        formato = QTextCharFormat()
        formato.setForeground(self.msgColors[cliente_ip])
        formato.setFontWeight(QFont.Bold)

        #user = getpass.getuser()
        self.text_MSGCHAT.setCurrentCharFormat(formato)
        self.text_MSGCHAT.append('<'+str(cliente_ip)+'>: '+ str(mensagem_dcripto))

        self.text_MSGCHAT_CRIPTO.setCurrentCharFormat(formato)
        self.text_MSGCHAT_CRIPTO.append('<'+str(cliente_ip)+'>: '+ str(mensagem_cripto))

    def encripta_RC4(self, chave_, mensagem):
        tamMsg = len(mensagem)
        cifrado_ = (ctypes.c_ubyte * tamMsg)()
        self.rc4_functions.cript(chave_.encode(), mensagem.encode(), cifrado_, tamMsg)
        return bytes(cifrado_)
    
    def decripta_RC4(self, chave_, mensagem):
        cifrado_ = bytes.fromhex(mensagem)
        tamMsg = len(mensagem)
        decifrado_ = (ctypes.c_ubyte * tamMsg)()
        decifrado_ = self.rc4_functions.cript(chave_, cifrado_, decifrado_, tamMsg)
        decifrado_ = bytes(decifrado_)
        return decifrado_

    def notify_box(self, campo):
        msg_notify = QMessageBox(self)
        msg_notify.setText("Preencha o(a) "+campo)
        msg_notify.exec()

    def enviar_mensagem(self, identidade, opt_Algoritmo):
        mensagem = str(self.text_MSG.text())
        chave_ = str(self.text_KEY.text())
        
        if mensagem == "":
            return

        if chave_ == "":
            self.notify_box("Chave de Criptografia")
            return

        if opt_Algoritmo == 'SDES':
            print(mensagem, chave_)
            buffer = create_string_buffer(8)
            self.sdes_functions.cript(chave_.encode(), mensagem.encode(), buffer)
            mensagem_cripto = bytes(buffer.value)
            self.envia_mensagemCHAT(str(buffer.value.decode()), mensagem, self.local_IP.text())


        elif opt_Algoritmo == 'RC4':
            mensagem_cripto = RC4(chave_.encode(), mensagem.encode())
            self.envia_mensagemCHAT(mensagem_cripto.hex(), mensagem, self.local_IP.text())

        self.Cliente.write(mensagem_cripto)

        self.text_MSG.clear()

    def get_instancia(cls):
        if not cls.__instancia__:
            cls.__instancia__= super().get_instancia(cls)
        return cls.__instancia__

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = mainWindow()
    janela.show()
    sys.exit(app.exec_())
