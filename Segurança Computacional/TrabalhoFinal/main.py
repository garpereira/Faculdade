from rc4 import RC4

import sys
import os
import getpass
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
from ctypes import *
import ctypes
import socket

class mainWindow(QMainWindow):

    __instancia__: None

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
        self.MyHN = socket.gethostname()
        self.MyIP = socket.gethostbyname(self.MyHN)

        # Compilando os Codigos C
        self.compilaCodigos()

        # Campo de IP ORIGEM
        self.seu_IP_label = QLabel(self)
        self.seu_IP_label.setText('IP Origem')
        self.seu_IP_label.setGeometry(10, 38, 120, 20)
        self.seu_IP_label.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(7)
        self.seu_IP_label.setFont(font)

        self.local_IP = QLineEdit(self)
        self.local_IP.setPlaceholderText(str(self.MyIP))
        self.local_IP.setGeometry(10, 10, 120, 30)
        self.local_IP.setReadOnly(True)

        # Campo de IP DESTINO
        self.text_IP = QLineEdit(self)
        self.text_IP.setPlaceholderText('Digite o IP Destino')
        self.text_IP.setGeometry(170, 10, 120, 30)
        #self.text_IP.textChanged.connect()

        # Botão Conectar
        self.btn_Conectar = QPushButton('Conectar', self)
        self.btn_Conectar.setGeometry(290, 10, 100, 30)
        
        # Campo de CHAVE CRIPTOGRAFADORA
        self.text_KEY = QLineEdit(self)
        self.text_KEY.setPlaceholderText('Digite a Chave Cripto')
        self.text_KEY.setGeometry(10, 70, 280, 30)
        self.text_KEY.setMaxLength(10)
        self.text_KEY.setValidator(QIntValidator(self))

        # Caixa de Seleção do Algoritmo
        self.opt_ALGORITHMS = QComboBox(self)
        self.opt_ALGORITHMS.addItems(['SDES', 'RC4'])
        self.opt_ALGORITHMS.setGeometry(290, 70, 100, 30)
        self.opt_ALGORITHMS.currentIndexChanged.connect(lambda: self.updateTypeKEY(self.opt_ALGORITHMS.currentText()))

        # Titulo do Chat
        self.text_MSGCHAT_LABEL = QLabel(self)
        self.text_MSGCHAT_LABEL.setText('BATE PAPO UOL')
        self.text_MSGCHAT_LABEL.setGeometry(10, 110, 380, 30)
        self.text_MSGCHAT_LABEL.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(15)
        self.text_MSGCHAT_LABEL.setFont(font)

        # Chat 1
        self.text_MSGCHAT = QTextEdit(self)
        self.text_MSGCHAT.setGeometry(10, 140, 380, 170)
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
        self.text_MSGCHAT_CRIPTO.setGeometry(10, 360, 380, 170)
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
        self.text_MSG.setGeometry(10, 550, 280, 30)
        self.text_MSG.installEventFilter(self)
        self.text_MSG.setValidator(QIntValidator(self))
        self.text_MSG.setMaxLength(8)

        # Botão Enviar mensagem
        self.btn_Enviar = QPushButton('Enviar', self)
        self.btn_Enviar.setGeometry(290, 550, 100, 30)
        self.btn_Enviar.clicked.connect(lambda: self.enviar_mensagem('servidor', self.opt_ALGORITHMS.currentText()))

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress and obj is self.text_MSG:
            if event.key() == Qt.Key_Return:
                self.enviar_mensagem('servidor', self.opt_ALGORITHMS.currentText())
                return True
            return False
        return False

    def updateTypeKEY(self, OPT):

        regex = QRegExp("[A-Za-z0-9!@#$%&*()_+{}:<>?]+")
        regex2 = QRegExp("[A-Za-z0-9!@#$%^&*()_+{}:<>? ]+")

        validator = QRegExpValidator(regex, self)
        validator2 = QRegExpValidator(regex2, self)

        if OPT == 'SDES':
            self.text_KEY.clear()
            self.text_KEY.setValidator(QIntValidator(self))
            self.text_KEY.setMaxLength(10)

            self.text_MSG.clear()
            self.text_MSG.setValidator(QIntValidator(self))
            self.text_MSG.setMaxLength(8)
            
        elif OPT == 'RC4':
            self.text_KEY.clear()
            self.text_KEY.setValidator(validator)
            self.text_KEY.setMaxLength(256)

            self.text_MSG.clear()
            self.text_MSG.setValidator(validator2)
            self.text_MSG.setMaxLength(256)

    def printaERRO(self, resultado):
        if resultado.returncode == 0:
            print("Compilação bem-sucedida.")
        else:
            print("Ocorreu um erro durante a compilação.")
            print("Saída de erro:", resultado.stderr)

    def compilaCodigos(self):
        comandos = [
            ['gcc', '-shared', '-o', 'sdes.so', '-fPIC', 'sdes.c'],
            ['gcc', '-shared', '-o', 'rc4.so', '-fPIC', 'rc4.c']
        ]
        paths = ['sdes/', 'rc4/']

        for i in range(len(comandos)):
            original_path = os.getcwd()
            os.chdir(paths[i])
            resultado = subprocess.run(comandos[i], capture_output=True, text=True)
            self.printaERRO(resultado)
            os.chdir(original_path)

        try:
            self.so_des = "./sdes/sdes.so"
            self.sdes_functions = CDLL(self.so_des)

            self.so_rc4 = "./rc4/rc4.so"
            self.rc4_functions = CDLL(self.so_rc4)
            self.rc4_functions.argtypes = [
                c_char_p,  # key
                c_char_p,  # plaintext
                ctypes.POINTER(ctypes.c_ubyte), # ciphertext
                ctypes.c_int
            ]
            self.rc4_functions.restype = None

        except:
            print("deu ruim padrin")
            None

    def conectar(self):
        pass
    
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

    def abrirLOG(self):
        self.chatLOG = open("chatLOG.txt", "r", encoding='utf-8')
    
    def fecharLOG(self):
        self.chatLOG.close()

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
            buffer = create_string_buffer(8)
            self.sdes_functions.cript(chave_.encode(), mensagem.encode(), buffer)
            mensagem_cripto = str(buffer.value.decode())

        if opt_Algoritmo == 'RC4':
            #cifrado_ = self.encripta_RC4(chave_, mensagem).hex()
            mensagem_cripto = RC4(chave_.encode(), mensagem.encode())
        
        #só pra ver o dcript
        if opt_Algoritmo == 'SDES':
            print(f'MsgCriptSDES Python -> {mensagem_cripto}\n')
            self.sdes_functions.dcript(chave_.encode(), mensagem_cripto.encode(), buffer)
            mensagem_criptoD = buffer.value.decode()
            print(f'MsgDCriptSDES Python -> {mensagem_cripto}\n')

        if opt_Algoritmo == 'RC4':
            print(f'MsgCriptRC4 Python -> {mensagem_cripto}\n')
            mensagem_criptoD = RC4(chave_.encode(), mensagem_cripto).decode()
            print(f'MsgDCriptRC4 Python -> {mensagem_cripto}\n')

        if identidade == 'servidor':
            cor = QColor(255, 0 ,0)

        elif identidade == 'cliente':
            cor = QColor(0, 0, 255)

        formato = QTextCharFormat()
        formato.setForeground(cor)
        formato.setFontWeight(QFont.Bold)

        user = getpass.getuser()
        self.text_MSGCHAT.setCurrentCharFormat(formato)
        self.text_MSGCHAT.append('<'+str(user)+'>: '+ str(mensagem))

        self.text_MSGCHAT_CRIPTO.setCurrentCharFormat(formato)
        self.text_MSGCHAT_CRIPTO.append('<'+str(user)+'>: '+ str(mensagem_cripto))

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
