import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
from ctypes import *
#import sdes

class mainWindow(QMainWindow):

    chave_rc4 = 'teste'

    __instancia__: None

    def __init__(self):
        super().__init__()
        screen_geo = QDesktopWidget().availableGeometry()
        x = (screen_geo.width() - self.width()) / 2
        y = (screen_geo.height() - self.height()) / 2

        self.setGeometry(x, y, 400, 600) #posicao x, y, largura, altura
        self.setWindowTitle('CHATZAO DOS CRIA')

        self.text_IP = QTextEdit(self)
        self.text_IP.setPlaceholderText('Digite o IP Destino')
        self.text_IP.setGeometry(10, 10, 280, 30)

        self.btn_Conectar = QPushButton('Conectar', self)
        self.btn_Conectar.setGeometry(290, 10, 100, 30)
        
        self.text_KEY = QTextEdit(self)
        self.text_KEY.setPlaceholderText('Digite a Chave Cripto')
        self.text_KEY.setGeometry(10, 70, 280, 30)

        self.opt_ALGORITHMS = QComboBox(self)
        self.opt_ALGORITHMS.addItems(['SDES', 'RC4'])
        self.opt_ALGORITHMS.setGeometry(290, 70, 100, 30)

        # self.checkbox_RC4 = QCheckBox('RC4', self)
        # self.checkbox_RC4.setGeometry(320, 50, 100, 30)

        # self.checkbox_SDES = QCheckBox('SDES', self)
        # self.checkbox_SDES.setGeometry(320, 80, 100, 30)

        self.text_MSGCHAT = QTextEdit(self)
        self.text_MSGCHAT.setGeometry(10, 110, 380, 400)

        scrollbar = QScrollBar(self)
        scrollbar.setGeometry(380, 200, 20, 300)
        self.text_MSGCHAT.setVerticalScrollBar(scrollbar)

        self.text_MSG = QTextEdit(self)
        self.text_MSG.setPlaceholderText('Escreva sua mensagem')
        self.text_MSG.setGeometry(10, 540, 280, 30)
        self.text_MSG.installEventFilter(self)

        self.btn_Enviar = QPushButton('Enviar', self)
        self.btn_Enviar.setGeometry(290, 540, 100, 30)
        self.btn_Enviar.clicked.connect(lambda: self.enviar_mensagem('servidor'))

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress and obj is self.text_MSG:
            if event.key() == Qt.Key_Return:
                self.enviar_mensagem('servidor')
                return True
            return False
        return False
    
    def conectar(self):
        pass

    def cript_rc4(self, mensagem):
        pass

    def enviar_mensagem(self, identidade):
        #01010101
        mensagem = self.text_MSG.toPlainText()
        chave_sdes = '1000000000'

        so_des = "./sdes/sdes.so"
        sdes_functions = CDLL(so_des)
            
        #print(c_char_p("10001001"))
        mensagem = sdes_functions.cript(bytes(chave_sdes, encoding='utf-8'), bytes(mensagem, encoding='utf-8'))

        if identidade == 'servidor':
            cor = QColor(255, 0 ,0)

        elif identidade == 'cliente':
            cor = QColor(0, 0, 255)

        formato = QTextCharFormat()
        formato.setForeground(cor)
        formato.setFontWeight(QFont.Bold)

        self.text_MSGCHAT.setCurrentCharFormat(formato)
        self.text_MSGCHAT.append(str(mensagem))
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
